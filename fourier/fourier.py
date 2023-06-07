import cv2
import numpy as np
import math

def norm(img):
    ret_val = img/img.max()
    return ret_val


def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global refPt, cropping
	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDOWN:
		refPt = [(x, y)]
		cropping = True
	# check to see if the left mouse button was released
	elif event == cv2.EVENT_LBUTTONUP:
		# record the ending (x, y) coordinates and indicate that
		# the cropping operation is finished
		refPt.append((x, y))
		cropping = False
		# draw a rectangle around the region of interest
		cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
		cv2.imshow("image", image)


cv2.setMouseCallback("image", click_and_crop)


img = cv2.imread("img.jpg", cv2.IMREAD_GRAYSCALE)
img  = cv2.resize(img, (600,600))

img_fft = np.fft.fftshift(np.fft.fft2(img))
img_fft_vis = norm(np.log(abs(img_fft)))

img_fft_mod = img_fft
for i in range(img_fft_mod.shape[0]):
    for j in range(img_fft_mod.shape[1]):
        if math.sqrt((i-300)**2 + (j-300)**2) <= 20:
            img_fft_mod[i][j] = 1
img_fft_mod_vis = norm(np.log(abs(img_fft_mod)))

recovered = abs(np.fft.ifft2(img_fft_mod))
recovered = norm(recovered)

cv2.imshow("orig", img)
cv2.imshow("fft_log", img_fft_vis)
cv2.imshow("fft_log_mod", img_fft_mod_vis)
cv2.imshow("recovered", recovered)

cv2.waitKey(-1)