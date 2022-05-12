import cv2
import numpy as np
import random

NUM_PTS = 30


points = [(random.randint(0, 899), random.randint(0, 899)) for x in range(NUM_PTS)] 

for it in range(0, 1000):
    image = np.zeros((900,900,3))

    for idx, point in enumerate(points):
        xi = np.random.choice([1,-1])
        yi = np.random.choice([1,-1])
        points[idx] = (point[0]+xi, point[1]+yi)
        
    for point in points:
        cv2.circle(image, point, 5, (255,0,0), 3)
    for point1, point2 in zip(points[:-1], points[1:]):
        cv2.line(image, point1, point2, (255,255,255))

    cv2.imshow("output", image)
    cv2.waitKey(10)