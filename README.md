# Gesture-Controlled-Virtual-Mouse
 Python program that enables gesture-based control of the computer mouse using hand tracking and image processing. The program utilizes Mediapipe for hand tracking, OpenCV for image processing, and PyAutoGUI for mouse cursor control, allowing users to move the cursor and perform clicks through hand gestures.

## Table of Contents

- [Python libraries used](#Python-libraries-used)
- [Installation](#installation)
- [Usage](#usage)
- [Supported Gestures](#supported-gestures)
- [Exiting the Program](#exiting-the-program)
- [Contributing](#contributing)
- [License](#license)


Python libraries used:

- **Mediapipe** for hand tracking
- **OpenCV** for image processing
- **PyAutoGUI** for mouse cursor control

## Installation

Before using this program, ensure that you have Python 3 installed on your computer. Next, install the necessary libraries by running the following command:

```
pip install mediapipe opencv-python pyautogui
```

## Usage
To use the program, follow these steps:

Run the virtualmouse.py file in your Python environment:
```
python virtualmouse.py
```
Your computer's default camera will activate, and the program will start detecting your hand movements.

Move your hand in the air to control the mouse cursor. The cursor will follow the position of your middle finger tip.

To perform a left mouse click, close your thumb finger to your index finger. The program will detect this gesture and click.

## Supported Gestures
The program recognizes two key hand gestures:

  - **Moving the Mouse Cursor:** Move your hand in the air to move the mouse cursor on the screen. The cursor will move to the position of your middle finger tip.

  - **Clicking the Mouse:** Close your thumb finger to your index finger to simulate a mouse click. The program will automatically detect the gesture and perform a left click.

## Exiting the Program
To exit the program, simply snap your thumb and middle finger together. (Thanos Snap)

## Contributors
Rupin Ajay (rupinajay@gmail.com), Rudra Panda(rudra.panda73@gmail.com)

We welcome contributions to this project. If you'd like to add features, fix bugs, or make improvements, please feel free to fork the repository and submit a pull request. Your contributions are valuable and will help enhance the functionality of this gesture-controlled mouse.

License
This project is licensed under the MIT License. You are free to use, modify, and distribute this software, subject to the terms of the license.

If you have any questions, encounter issues, or wish to discuss this project further, please don't hesitate to reach out. Enjoy using your gesture-controlled mouse!

