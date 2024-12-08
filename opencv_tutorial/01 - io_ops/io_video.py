import cv2
import os

# read video
video_path = os.path.join(".", "data", "monkey.mp4")

video = cv2.VideoCapture(video_path)

# visualize video
ret = True
while ret:
    ret, frame = video.read()

    if ret:
        frame = cv2.resize(frame, (800, 600))
        cv2.imshow("video", frame)
        cv2.waitKey(40)

video.release()
cv2.destroyAllWindows()
