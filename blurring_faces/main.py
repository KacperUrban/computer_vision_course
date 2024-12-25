import cv2
import mediapipe as mp
import os
import numpy as np


# read image
img = cv2.imread(os.path.join('.', 'face.jpg'))
img = cv2.resize(img, (800, 600))
H, W, _ = img.shape

# detect faces
detector = mp.solutions.face_detection

with detector.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detector:
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_detector.process(img_rgb)

    if results:
        for detection in results.detections:
            print(f"Score: {np.round(detection.score[0], 4) * 100}%")
            loc_data = detection.location_data.relative_bounding_box
            x1, y1, w, h = int(loc_data.xmin * W), int(loc_data.ymin * H), int(loc_data.width * W), int(loc_data.height * H)
            x1_text = x1
            y1_text = y1 - 10

            img = cv2.putText(img, f"Score: {np.round(detection.score[0], 4) * 100}%", (x1_text, y1_text), cv2.FONT_HERSHEY_SIMPLEX, 
                              0.8, (0, 255, 0), 3)
            img = cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 4)
            img[y1:y1 + h, x1:x1 + w, :] = cv2.blur(img[y1:y1 + h, x1:x1 + w, :], (50, 50))

cv2.imshow('image', img)
cv2.waitKey(0)
