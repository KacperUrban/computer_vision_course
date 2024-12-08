import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'cat1.jpg'))

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("classic", img)
cv2.imshow("rgb image", img_rgb)
cv2.imshow("grayscale image", img_gray)
cv2.imshow("hsv image", img_hsv)
cv2.waitKey(0)
