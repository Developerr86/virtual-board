import cv2
import mediapipe as mp
import math
import time
import tkinter as tk

def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def get_display_size():
    root = tk.Tk()
    display_width = root.winfo_screenwidth()
    display_height = root.winfo_screenheight()
    root.destroy()
    return display_width, display_height

def scale_points(points, orig_size, new_size):
    orig_width, orig_height = orig_size
    new_width, new_height = new_size
    return [(int(x * new_width / orig_width), int(y * new_height / orig_height)) for (x, y) in points]

def is_pointing_finger_up(hand_landmarks):
    # Check if the index finger is up and other fingers are down
    if (hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y and  # Index finger tip is above PIP joint
        hand_landmarks.landmark[12].y > hand_landmarks.landmark[10].y and  # Middle finger tip is below PIP joint
        hand_landmarks.landmark[16].y > hand_landmarks.landmark[14].y and  # Ring finger tip is below PIP joint
        hand_landmarks.landmark[20].y > hand_landmarks.landmark[18].y):  # Pinky finger tip is below PIP joint
        return True
    return False

frame_width = 854
frame_height = 480
orig_size = (frame_width, frame_height)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (frame_width, frame_height))

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

draw_points = []
draw_times = []

# Get display size and calculate window size
display_width, display_height = get_display_size()
window_width = int(display_width * 0.9)
window_height = int(display_height * 0.9)

# Control recording with a boolean variable
recording = False  # Set this to False to stop recording

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Mirror the video capture
    frame = cv2.flip(frame, 1)

    # Resize the frame for display
    new_size = (window_width, window_height)
    display_frame = cv2.resize(frame, new_size)

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(display_frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Get the coordinates of thumb tip and index finger tip
            index_tip = (int(hand_landmarks.landmark[8].x * frame.shape[1]), int(hand_landmarks.landmark[8].y * frame.shape[0]))

            if is_pointing_finger_up(hand_landmarks):
                draw_points.append(index_tip)
                draw_times.append(time.time())

    # Scale points to new size
    scaled_points = scale_points(draw_points, orig_size, new_size)

    # Draw continuous lines between consecutive points if the time difference is less than 2 seconds
    for i in range(1, len(scaled_points)):
        if draw_times[i] - draw_times[i - 1] < 2:
            cv2.line(display_frame, scaled_points[i - 1], scaled_points[i], (0, 255, 0), 5)

    if recording:
        out.write(frame)  # Write the original frame into the file

    cv2.imshow('Frame', display_frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):
        draw_points = []  # Clear the drawing
        draw_times = []  # Clear the draw times
    elif key == ord('r'):
        recording = not recording  # Toggle recording

cap.release()
out.release()  # Release the VideoWriter object
cv2.destroyAllWindows()
