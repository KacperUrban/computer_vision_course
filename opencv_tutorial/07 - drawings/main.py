import cv2
import os

img = cv2.imread(os.path.join('.', 'data', 'whiteboard.jpg'))
img = cv2.resize(img, (800, 600))

# line
cv2.line(img, (300, 200), (400, 100), (255, 0, 0), 5)
cv2.line(img, (500, 200), (400, 100), (255, 0, 0), 5)
cv2.line(img, (300, 200), (200, 300), (255, 0, 0), 5)
cv2.line(img, (300, 400), (200, 300), (255, 0, 0), 5)
cv2.line(img, (300, 400), (400, 500), (255, 0, 0), 5)
cv2.line(img, (500, 400), (400, 500), (255, 0, 0), 5)
cv2.line(img, (500, 400), (600, 300), (255, 0, 0), 5)
cv2.line(img, (500, 200), (600, 300), (255, 0, 0), 5)

# rectangle
cv2.rectangle(img, (300, 200), (500, 400), (0, 0, 255), -1)

# circles
cv2.circle(img, (300, 200), 15, (255, 0, 0), 5)
cv2.circle(img, (500, 200), 15, (255, 0, 0), 5)
cv2.circle(img, (300, 400), 15, (255, 0, 0), 5)
cv2.circle(img, (500, 400), 15, (255, 0, 0), 5)
cv2.circle(img, (400, 300), 200, (0, 255, 0), 5)

cv2.imshow('whiteboard', img)
cv2.waitKey(0)