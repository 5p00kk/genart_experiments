#shape[0] row
#shape[1] col

import cv2
import numpy as np
import math

# Image size
SIZE = 900
X_FUNC = lambda t: math.sin(t)+math.sin(2*t*t)*math.cos(t)
Y_FUNC = lambda t: math.cos(t)+math.sin(t*t)

# Video writer
video_fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video_writer = cv2.VideoWriter("output.mp4",video_fourcc, 100, (SIZE,SIZE), False)

# Create image with text
image = np.zeros((SIZE, SIZE), np.uint8)
image = cv2.putText(image, "x = sin(t)+sin(2t^2)*cos(t)", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 164, 1, cv2.LINE_AA)
image = cv2.putText(image, "y = cos(t)+sin(t^2)", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 164, 1, cv2.LINE_AA)

# Create time vector
ts = [x for x in np.arange(0,1000,0.0001)]

for i, t in enumerate(ts):
    # Equation
    x = X_FUNC(t)
    y = Y_FUNC(t)
    # FP coordinates
    coord = (x, y)
    # Convert to image coordinates (do it nicer)
    coord_int = (int((coord[0]/2+1)*(SIZE/2-1)), int((coord[1]/2+1)*(SIZE/2-1)))
    
    image[coord_int[0], coord_int[1]] = 255
    # Update image
    #if i>50000:
    #    if image[coord_int[0], coord_int[1]] <= 255-10:
    #        image[coord_int[0], coord_int[1]] += 5
    # Add frame to video
    if i%50==0:
        #video_writer.write(image)
        #cv2.imwrite("itr_"+str(i)+".png", image)
        cv2.imshow("out", image)
        cv2.waitKey(1)

# Finish up
video_writer.release()
cv2.imwrite("final.png", image)