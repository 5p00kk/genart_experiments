#shape[0] row
#shape[1] col

import cv2
import numpy as np
import math
from plot_functions import line_plot
from utils import sigmoid
import os

# Execution definitions
SIZE = 900
DURATION = 700
STEP = 0.0001
INCREMENTAL = True
SHOW_IMAGE = True
SAVE_VIDEO = False
SAVE_HSV = False
H = 133
S = 255
# Function definitions
X_FUNC = lambda t: math.sin(t)+math.sin(2*t*t)*math.cos(t)
X_MIN = -2
X_RANGE = 4
Y_FUNC = lambda t: math.cos(t)+math.sin(t*t)
Y_MIN = -2
Y_RANGE = 4

# Create output folder if it's not there
if not os.path.exists("output"):
  os.makedirs("output")

# Video writer
video_writer = None
if SAVE_VIDEO:
  video_fourcc = cv2.VideoWriter_fourcc(*"mp4v")
  video_writer = cv2.VideoWriter("output/video.mp4",video_fourcc, 60, (SIZE,SIZE), False)

# Create image with text
image = np.zeros((SIZE, SIZE), np.uint8)
image = cv2.putText(image, "x = sin(t)+sin(2t^2)*cos(t)", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 164, 1, cv2.LINE_AA)
image = cv2.putText(image, "y = cos(t)+sin(t^2)", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 164, 1, cv2.LINE_AA)

# Create time vector
ts = [x for x in np.arange(0, DURATION, STEP)]
image_out = line_plot(ts, (X_FUNC, X_MIN, X_RANGE), (Y_FUNC, Y_MIN, Y_RANGE), image, video_writer, SHOW_IMAGE, INCREMENTAL)

# Finish up
if SAVE_VIDEO:
  video_writer.release()

# Save final images
blank = np.zeros((SIZE, SIZE), np.uint8)
merged_b = cv2.merge([image_out, blank, blank])
merged_g = cv2.merge([blank, image_out, blank])
merged_r = cv2.merge([blank, blank, image_out])
# Prepare HSV
if SAVE_HSV:
  h = H*np.ones((SIZE, SIZE), np.uint8)
  s = S*np.ones((SIZE, SIZE), np.uint8)
  merged_hsv = cv2.merge([h, s, image_out])
  merged_hsv = cv2.cvtColor(merged_hsv, cv2.COLOR_HSV2BGR)

cv2.imwrite("output/final.png", image_out)
cv2.imwrite("output/final_r.png", merged_r)
cv2.imwrite("output/final_g.png", merged_g)
cv2.imwrite("output/final_b.png", merged_b)
if SAVE_HSV:
  cv2.imwrite("output/final_hsv.png", merged_hsv)