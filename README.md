# Human-Pose-Detection

# Overview

This project implements real-time human pose detection using Mediapipe Pose model and OpenCV. The system can : 

1. Detct human body keypoints (eg. shoulders, elbows, knees, etc)

2. Work with live webcam feeds or pre-recorded videos.

3. Save the output video with pose overlays.

This project is designed to run smoothly in Google Colab (pre recorded videos) and local environments (Visual studio code etc).

# Features

1. Real time pose detection using Mediapipe.

2. Works with webcam & video files.

3. Google colab & local machine.

4. Draws keypoints & skeleton connections.

5. Saves processed video output.

# Running the Project

1. <ins> Run on a Local Machine</ins>

        detect_pose(0) # Use webcam
               #or
         detect_pose("path/to/video.mp4") # Process a pre-recorded video
   press 'q' to exit the webcam stream

2. <ins> Run in Google Colab</ins>

Since Google Colab does not support direct webcam access, use a pre-recorded video:

         from google.colab.patches import cv2_imshow # Required for Colab 
         display
         detect_pose("path/to/video.mp4", output_file="output.mp4", 
         display=True)
After processing, download the output video:

         from google.colab import files
         files.download("output.mp4")

# Code Explanation
