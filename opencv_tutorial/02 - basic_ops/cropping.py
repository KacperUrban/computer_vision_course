import os
import cv2

img_path = os.path.join('.', 'data', 'dog2.jpg')
img = cv2.imread(img_path)
img_cropped = img[60:140, 50:200]

print(img.shape)

cv2.imshow('dog', img)
cv2.imshow('dog cropped', img_cropped)
cv2.waitKey(0)
