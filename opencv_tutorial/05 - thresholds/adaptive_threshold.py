import cv2
import os

img = cv2.imread(os.path.join('.', 'data', 'handwritten.png'))
bin_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(bin_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 6)

cv2.imshow("orginal", img)
cv2.imshow("thresh", thresh)
cv2.waitKey(0)