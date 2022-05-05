#shape[0] row
#shape[1] col

import cv2
import numpy as np
import math

SIZE = 900
video_FourCC = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output.mp4",video_FourCC, 100, (SIZE,SIZE), False)
image = np.zeros((SIZE, SIZE), np.uint8)

image = cv2.putText(image, "x = sin(t)+sin(2t^2)*cos(t)", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 164, 1, cv2.LINE_AA)
image = cv2.putText(image, "y = cos(t)+sin(t^2)", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 164, 1, cv2.LINE_AA)

ts = [x for x in np.arange(0,35,0.0001)]

i = 0
for t in ts:
    i=i+1
    x = math.sin(t)+math.sin(2*t*t)*math.cos(t)
    y = math.cos(t)+math.sin(t*t)
    coord = (x, y)
    coord_int = (int((coord[0]/2+1)*(SIZE/2-1)), int((coord[1]/2+1)*(SIZE/2-1)))
    image[coord_int[0], coord_int[1]] = 255
    if i%150==0:
        out.write(image)
        #cv2.imshow("test", image)
        #cv2.waitKey(1)

out.release()
cv2.imwrite("test_0.png", image)