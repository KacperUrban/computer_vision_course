import cv2
import os

# read image
path_img = os.path.join(".", "data", "dog1.jpg")

img = cv2.imread(path_img)

# write image
path_img_out = os.path.join(".", "data", "dog1_out.jpg")
cv2.imwrite(path_img_out, img)

# visualize image
cv2.imshow("image", img)
cv2.waitKey(0)
