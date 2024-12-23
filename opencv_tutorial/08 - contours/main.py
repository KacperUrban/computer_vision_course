import os
import cv2


img = cv2.imread(os.path.join('.', 'data', 'birds.jpg'))
img = cv2.resize(img, (800, 600))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt) > 200:
        x1, y1, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)
cv2.imshow('image', img)
cv2.waitKey(0)