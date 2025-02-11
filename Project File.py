!pip install mediapipe opencv-python numpy

# Import required libraries
import cv2
import mediapipe as mp
import numpy as np
import time
from google.colab.patches import cv2_imshow  # Required for Google Colab display

# Initialize Mediapipe Pose model
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# Function to process video and detect human pose
def detect_pose(video_source='/content/WIN_20250210_17_58_16_Pro.mp4', output_file="output.mp4", display=True):
    cap = cv2.VideoCapture(video_source)  # 0 for webcam or path to video file

    # Get video properties for saving output
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    fps = int(cap.get(cv2.CAP_PROP_FPS)) if cap.get(cv2.CAP_PROP_FPS) > 0 else 30

    # Define video writer if saving output
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

    # Set up Mediapipe Pose
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Convert frame to RGB (required for Mediapipe)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(frame_rgb)

            # Draw pose landmarks
            if results.pose_landmarks:
                mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Write frame to output video file
            out.write(frame)

            # Display frame in Google Colab
            if display:
                cv2_imshow(frame)

            # Delay for visibility
            time.sleep(0.03)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    print(f"Processing complete! Output saved as {output_file}")

# To use webcam, run: detect_pose(0)
# To use a video file, replace '0' with 'path/to/video.mp4'
detect_pose('/content/WIN_20250210_17_58_16_Pro.mp4', output_file="output.mp4", display=True)
