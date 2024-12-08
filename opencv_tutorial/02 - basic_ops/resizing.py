import os
import cv2

img_path = os.path.join('.', 'data', 'cat1.jpg')
img = cv2.imread(img_path)
resized_img = cv2.resize(img, (580, 348)) # width x heigth

print(img.shape)
print(resized_img.shape)

cv2.imshow('image', img)
cv2.imshow('resized image', resized_img)
cv2.waitKey(0)
