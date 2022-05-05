#shape[0] row
#shape[1] col

import cv2
import numpy as np
import math

# Image size
SIZE = 900

# Video writer
video_fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video_writer = cv2.VideoWriter("output.mp4",video_fourcc, 100, (SIZE,SIZE), False)

# Create image with text
image = np.zeros((SIZE, SIZE), np.uint8)
image = cv2.putText(image, "x = sin(t)+sin(2t^2)*cos(t)", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 164, 1, cv2.LINE_AA)
image = cv2.putText(image, "y = cos(t)+sin(t^2)", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 164, 1, cv2.LINE_AA)

# Create time vector
ts = [x for x in np.arange(0,35,0.0001)]

for i, t in enumerate(ts):
    # Equation
    x = math.sin(t)+math.sin(2*t*t)*math.cos(t)
    y = math.cos(t)+math.sin(t*t)
    # FP coordinates
    coord = (x, y)
    # Convert to image coordinates (do it nicer)
    coord_int = (int((coord[0]/2+1)*(SIZE/2-1)), int((coord[1]/2+1)*(SIZE/2-1)))
    # Update image
    image[coord_int[0], coord_int[1]] = 255
    # Add frame to video
    if i%150==0:
        video_writer.write(image)

# Finish up
video_writer.release()
cv2.imwrite("final.png", image)