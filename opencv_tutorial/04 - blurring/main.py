import cv2
import os
import numpy as np

img = cv2.imread(os.path.join('.', 'data', 'player.jpg'))
k_size = 7
img_blur = cv2.blur(img, (k_size, k_size))
img_gauss = cv2.GaussianBlur(img, (k_size, k_size), 3)
img_median = cv2.medianBlur(img, k_size)

images_1 = np.concatenate((img, img_blur), axis=1)
images_2 = np.concatenate((img_gauss, img_median), axis=1)
images = np.concatenate((images_1, images_2), axis=0)

images = cv2.resize(images, (1400, 900))
cv2.imshow("img", images)
cv2.waitKey(0)