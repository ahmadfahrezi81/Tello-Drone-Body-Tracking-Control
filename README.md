
# Tello Drone Body Tracking & Control

## Overview

This project allows you to control a Tello drone using body gestures. It utilizes computer vision techniques to track body movements and interprets specific gestures for drone control. The project uses the Tello drone, Python, and various libraries for computer vision and drone control.

## Prerequisites

- Python 3.9
- Tello drone
- Internet connection (for installing dependencies)

## Installation

1. Clone the project:

    ```bash
    git clone https://github.com/ahmadfahrezi81/Tello-Drone-Body-Tracking-Control.git
    cd tello-drone-body-gesture
    ```

2. Set up a virtual environment:

    ```bash
    python3.9 -m venv venv_name
    source venv_name/bin/activate
    ```

3. Install project dependencies:

    ```bash
    pip install absl-py==2.0.0
    pip install attrs==23.1.0
    pip install cffi==1.16.0
    pip install contourpy==1.2.0
    pip install cycler==0.12.1
    pip install djitellopy2==2.3
    pip install flatbuffers==23.5.26
    pip install fonttools==4.46.0
    pip install kiwisolver==1.4.5
    pip install matplotlib==3.8.2
    pip install mediapipe==0.10.9
    pip install numpy==1.26.2
    pip install opencv-contrib-python==4.8.1.78
    pip install opencv-python==4.8.1.78
    pip install packaging==23.2
    pip install Pillow==10.1.0
    pip install protobuf==3.20.3
    pip install pycparser==2.21
    pip install pyparsing==3.1.1
    pip install python-dateutil==2.8.2
    pip install six==1.16.0
    pip install sounddevice==0.4.6
    python pip install yagmail
    python pip install python-dotenv
    ```

    This installs all the required packages for the project.

4. Run the main script:

    ```bash
    python Tello.py
    ```

    The script will start capturing video and interpreting body gestures to control the drone.

5. Press 'q' to exit the program and safely land the drone.

## Dependencies

- [absl-py](https://pypi.org/project/absl-py/) (2.0.0)
- [attrs](https://pypi.org/project/attrs/) (23.1.0)
- [cffi](https://pypi.org/project/cffi/) (1.16.0)
- [contourpy](https://pypi.org/project/contourpy/) (1.2.0)
- [cycler](https://pypi.org/project/cycler/) (0.12.1)
- [djitellopy2](https://pypi.org/project/djitellopy2/) (2.3)
- [flatbuffers](https://pypi.org/project/flatbuffers/) (23.5.26)
- [fonttools](https://pypi.org/project/fonttools/) (4.46.0)
- [kiwisolver](https://pypi.org/project/kiwisolver/) (1.4.5)
- [matplotlib](https://pypi.org/project/matplotlib/) (3.8.2)
- [mediapipe](https://pypi.org/project/mediapipe/) (0.10.9)
- [numpy](https://pypi.org/project/numpy/) (1.26.2)
- [opencv-contrib-python](https://pypi.org/project/opencv-contrib-python/) (4.8.1.78)
- [opencv-python](https://pypi.org/project/opencv-python/) (4.8.1.78)
- [packaging](https://pypi.org/project/packaging/) (23.2)
- [Pillow](https://pypi.org/project/Pillow/) (10.1.0)
- [protobuf](https://pypi.org/project/protobuf/) (3.20.3)
- [pycparser](https://pypi.org/project/pycparser/) (2.21)
- [pyparsing](https://pypi.org/project/pyparsing/) (3.1.1)
- [python-dateutil](https://pypi.org/project/python-dateutil/) (2.8.2)
- [six](https://pypi.org/project/six/) (1.16.0)
- [sounddevice](https://pypi.org/project/sounddevice/) (0.4.6)

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute and make improvements! If you encounter any issues or have suggestions, please open an [issue](https://github.com/your-username/tello-drone-body-gesture/issues).

Happy coding!
