import cv2
import numpy as np
import math

def norm(img):
    ret_val = img/img.max()
    return ret_val

drawing = False

def m_callback(event, x, y, flags, param):
    global drawing, img_fft
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
    if drawing:
        print((x,y))

        RADIUS=20
        for i in range(x-RADIUS, x+RADIUS):
            for j in range(y-RADIUS, y+RADIUS):
                if math.sqrt((i-x)**2 + (j-y)**2) <= RADIUS:
                    img_fft[j][i] = 1


cv2.namedWindow("fft_log")
cv2.setMouseCallback("fft_log", m_callback)

img = cv2.imread("img.jpg", cv2.IMREAD_GRAYSCALE)
img  = cv2.resize(img, (600,600))

img_fft = np.fft.fftshift(np.fft.fft2(img))

# keep looping until the 'q' key is pressed
while True:

    img_fft_vis = norm(np.log(abs(img_fft)))

    recovered = abs(np.fft.ifft2(img_fft))
    recovered = norm(recovered)

    # display the image and wait for a keypress
    cv2.imshow("orig", img)
    cv2.imshow("fft_log", img_fft_vis)
    cv2.imshow("recovered", recovered)
    cv2.waitKey(1)