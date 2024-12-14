import cv2
import numpy as np
import os


img = cv2.imread(os.path.join('.', 'data', 'player.jpg'))
img_detc = cv2.Canny(img, 100, 200)
img_detc_d = cv2.dilate(img_detc, np.ones((3,3)))
img_detc_e = cv2.erode(img_detc_d, np.ones((2,2)))

images = np.concatenate((img_detc, img_detc_d), axis=1)
images = cv2.resize(images, (1200, 600))
images = np.concatenate((images, img_detc_e), axis=0)

cv2.imshow('orginal image', img)
cv2.imshow('transformed images', images)
cv2.waitKey(0)