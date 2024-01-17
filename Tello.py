import cv2, math, time, yagmail
import mediapipe as mp
from utils.PoseDetectorModule import PoseDetector
from djitellopy import Tello

import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

#input
id_number = input("Enter your ID/Badge number: ")
receiver_email = input("Enter your email address: ")
receiver_name = input("Enter your name: ")

# email setup
body = f"SOS Detected. Here are the coordinates and image captured:\n\n"
body += f"Receiver Name: {receiver_name}\n"
body += f"ID/Badge Number: {id_number}\n"

gmail_user = os.getenv('GMAIL_HOST')
gmail_password = os.getenv("GMAIL_PASSWORD")

coords = "43.6532 N, 79.3832 W" 

detector = PoseDetector(upBody=True)

def calAngle(lmList, p1, p2, p3, draw=True):
    if len(lmList) != 0:
        x1, y1 = lmList[p1][1:]
        x2, y2 = lmList[p2][1:]
        x3, y3 = lmList[p3][1:]
        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
        if angle < 0: angle += 360
        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
            cv2.line(img, (x2, y2), (x3, y3), (255, 0, 255), 2)
            cv2.circle(img, (x1, y1), 5, (255, 255, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 5, (255, 255, 0), cv2.FILLED)
            cv2.circle(img, (x3, y3), 5, (255, 255, 0), cv2.FILLED),
            cv2.putText(img, str(int(angle)), (x2 - 20, y2 - 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        return angle
    return 0

def calcDist(lmList, p1, p2, draw=True):
    if len(lmList) != 0:
        x1, y1 = lmList[p1][1:]
        x2, y2 = lmList[p2][1:]
        dist = math.hypot(x2 - x1, y2 - y1)
        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 4)
            cv2.circle(img, (x1, y1), 5, (255, 255, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 5, (255, 255, 0), cv2.FILLED)
            cv2.putText(img, str(int(dist)), (x2 + 20, y2 + 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)
        return dist
    return 0

tello = Tello()
tello.connect() 
battery_percentage = tello.get_battery() 
print("BATTERY PERCENTAGE: ", battery_percentage) 
tello.streamon()
tello.takeoff()
tello.move_up(80)
# time.sleep(30)

while True:    
    lr, fb, ud, rot = 0, 0, 0, 0
    img = tello.get_frame_read().frame
    img = cv2.flip(img, 1)
    img = detector.findPose(img, draw=False)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False)
    if lmList != 0:
        angleR = calAngle(lmList, 13, 11, 23, draw=False)
        angleL = calAngle(lmList, 24, 12, 14, draw=False)
        elbowR = calAngle(lmList, 15, 13, 11)
        elbowL = calAngle(lmList, 12, 14, 16)
        distR = calcDist(lmList, 12, 15)
        distL = calcDist(lmList, 11, 16)

        if 165 < angleR < 185 and not (165 < angleL < 185):
            cv2.putText(img, 'SOS Detected - Right Hand Raised', (50, 60), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 255), 2)          
            cv2.imwrite("sos_detected.jpg", img)

            try:
                yag = yagmail.SMTP(user=gmail_user, password=gmail_password)
                yag.send(
                    to=receiver_email,
                    subject="SOS Detected - Image and Coordinates",
                    contents= body + f" {coords}", 
                    attachments="sos_detected.jpg",
                )
                print("Email sent successfully")
            except:
                print("Error, email was not sent")

            fb = 40

        elif not (165 < angleR < 185) and 165 < angleL < 185:

            cv2.putText(img, 'SOS Detected - Left Hand Raised', (50, 60), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 255), 2)          
            cv2.imwrite("sos_detected.jpg", img)

            try:
                yag = yagmail.SMTP(user=gmail_user, password=gmail_password)
                yag.send(
                    to=receiver_email,
                    subject="SOS Detected - Image and Coordinates",
                    contents= body + f" {coords}", 
                    attachments="sos_detected.jpg",
                )
                print("Email sent successfully")
            except:
                print("Error, email was not sent")

            fb = 40
    

    tello.send_rc_control(lr, fb, ud, rot)
    cv2.imshow('window', img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        tello.land()
        tello.streamoff()
        tello.end()
        break
# cap.release()
cv2.destroyAllWindows()