import math
import numpy as np
import cv2

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def get_hsv(r, g, b):
  rgb = np.uint8([[[b, g, r]]])
  hsv = cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)
  return hsv