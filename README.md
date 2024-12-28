# Drawing Board with Hand Gestures

This project is a drawing board application that uses hand gestures for drawing, implemented using OpenCV, Mediapipe, and Tkinter. It supports functionalities like recording the drawing session, auto-cleaning the screen, and clearing the screen, with visual indicators for each feature.

## Features
- Draw using hand gestures: Draw on the screen by pointing your index finger while folding other fingers into a fist.
- Recording: Toggle recording of the drawing session.
- Auto-Clean: Enable or disable auto-clean mode where drawings fade out after 5 seconds.
- Clear Screen: Clear the drawing on the screen.
- Visual Indicators: Indicators for recording status, auto-clean mode, and screen cleared status.

## Requirements
- Python 3.x
- OpenCV
- Mediapipe
- Tkinter (comes with Python)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Developerr86/virtual-board
    cd drawing-board
    ```

2. Install the required libraries:
    ```bash
    pip install opencv-python mediapipe
    ```

## Usage
1. Run the script:
    ```bash
    python drawing_board.py
    ```

2. The application window will open. Use the following keys to control the features:
    - `r`: Toggle recording ON/OFF
    - `t`: Toggle auto-clean mode ON/OFF
    - `c`: Clear the screen
    - `q`: Quit the application

## Code Explanation
The application uses OpenCV to capture video from the webcam and Mediapipe for hand gesture detection. Tkinter is used to create a resizable window. The key functionalities are as follows:

- **Hand Gesture Detection**: Mediapipe detects the hand landmarks. Drawing happens if the index finger is up and other fingers are down.
- **Drawing**: Points are recorded and lines are drawn between consecutive points to create continuous drawing.
- **Recording**: Frames are saved into a video file if recording is enabled.
- **Auto-Clean**: Drawings fade out after 5 seconds if auto-clean mode is enabled.
- **Clear Screen**: All drawing points are cleared from the screen.
- **Visual Indicators**: Indicators for recording status, auto-clean mode, and screen cleared status are displayed on the screen.

## Contributing
Feel free to open issues or submit pull requests for improvements and bug fixes. Contributions are welcome!

## License
This project is licensed under the MIT License.
