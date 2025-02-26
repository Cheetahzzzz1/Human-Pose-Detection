import cv2
import mediapipe as mp
import numpy as np

# Initialize Mediapipe Pose module
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

def detect_pose(video_source=0, output_file="output.mp4", display=True):
    """
    Detects human pose using Mediapipe Pose model.
    
    Parameters:
    - video_source: 0 for webcam, or path to video file
    - output_file: Name of the output video file
    - display: If True, shows the video output in a window
    """

    cap = cv2.VideoCapture(video_source)  # Capture video (webcam or file)
    
    # Get video properties
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    fps = int(cap.get(cv2.CAP_PROP_FPS)) if cap.get(cv2.CAP_PROP_FPS) > 0 else 30

    # Define video writer to save the output
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  
    out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

    # Initialize Mediapipe Pose model
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break  # Exit if video ends

            # Convert frame to RGB (required for Mediapipe)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(frame_rgb)

            # Draw pose landmarks
            if results.pose_landmarks:
                mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Write frame to output video file
            out.write(frame)

            # Display the frame
            if display:
                cv2.imshow("Pose Detection", frame)

            # Exit when 'q' is pressed
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Processing complete! Output saved as {output_file}")

# Run pose detection (0 for webcam, or provide video file path)
detect_pose(0, output_file="output.mp4", display=True)