# Gesture-Controlled Screen Brightness

This project utilizes hand gestures to control the screen brightness. Using the MediaPipe library for hand tracking and OpenCV for image processing, it detects specific gestures and adjusts the screen brightness accordingly.

## Requirements

- Python 3.10.5
- Libraries: `numpy`, `mediapipe`, `opencv-python`, `screen_brightness_control`

## Installation

1. Clone this repository.
2. Install the required libraries using `pip`:
    ```
    pip install -r requirements.txt
    ```

## How it works

The code uses the webcam to capture the hand gestures. Once the hand landmarks are detected, it calculates the distance between two specific points on the hand to determine the brightness level. Changing the distance between these points alters the brightness on the screen.

## Usage

1. Run the Python script.
2. Make sure your hand is visible to the webcam.
3. Adjust the distance between your thumb and index finger to control the screen brightness.
4. Press 'q' to exit the program.

## Note

- This code assumes one hand is in the frame and controls brightness based on the distance between the thumb and index finger landmarks.

Feel free to contribute, modify, or improve this project!
