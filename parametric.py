#shape[0] row
#shape[1] col

import cv2
import numpy as np
import math
from plot_functions import line_plot
from utils import sigmoid

# Execution definitions
SIZE = 900
DURATION = 700
INCREMENTAL = True
SHOW_IMAGE = True
SAVE_VIDEO = False
# Function definitions
X_FUNC = lambda t: math.sin(t)+math.sin(2*t*t)*math.cos(t)
X_MIN = -2
X_RANGE = 4
Y_FUNC = lambda t: math.cos(t)+math.sin(t*t)
Y_MIN = -2
Y_RANGE = 4

# Video writer
video_writer = None
if SAVE_VIDEO:
  video_fourcc = cv2.VideoWriter_fourcc(*"mp4v")
  video_writer = cv2.VideoWriter("output.mp4",video_fourcc, 100, (SIZE,SIZE), False)

# Create image with text
image = np.zeros((SIZE, SIZE), np.uint8)
image = cv2.putText(image, "x = sin(t)+sin(2t^2)*cos(t)", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 164, 1, cv2.LINE_AA)
image = cv2.putText(image, "y = cos(t)+sin(t^2)", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 164, 1, cv2.LINE_AA)

# Create time vector
ts = [x for x in np.arange(0, DURATION, 0.0001)]
image_out = line_plot(ts, (X_FUNC, X_MIN, X_RANGE), (Y_FUNC, Y_MIN, Y_RANGE), image, video_writer, SHOW_IMAGE, INCREMENTAL)

# Finish up
video_writer.release()
cv2.imwrite("final.png", image_out)