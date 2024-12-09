import cv2
import os

img = cv2.imread(os.path.join('.', 'data', 'cat2.jpg'))
bin_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh_img = cv2.threshold(bin_img, 80, 255, cv2.THRESH_BINARY)
# blur_img = cv2.blur(thresh_img, (7, 7))
# _, thresh_img = cv2.threshold(bin_img, 80, 255, cv2.THRESH_BINARY)

cv2.imshow("cat_org", img)
cv2.imshow("cat_thresh", thresh_img)
cv2.waitKey(0)