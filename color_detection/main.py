import cv2
from PIL import Image

from utils import get_limits


yellow = [0, 255, 255]

lowerlimit, upperlimit = get_limits(yellow)

video = cv2.VideoCapture(0)
while True:
    ret, frame = video.read()
    hsvimage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsvimage, lowerlimit, upperlimit)
    maskpil  = Image.fromarray(mask)

    boundingbox = maskpil.getbbox()

    if boundingbox:
        x1, y1, x2, y2 = boundingbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

    cv2.imshow("Color detection", frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()