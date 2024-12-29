import cv2
import mediapipe as mp
import os
import numpy as np
import argparse

def detect_faces(img: np.ndarray, face_detector: mp.solutions.face_detection.FaceDetection) -> None:
    H, W, _ = img.shape
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_detector.process(img_rgb)

    if results.detections:
        for detection in results.detections:
            loc_data = detection.location_data.relative_bounding_box
            x1 = int(max(0, loc_data.xmin * W))
            y1 = int(max(0, loc_data.ymin * H))
            w = int(min(loc_data.width * W, W - x1))
            h = int(min(loc_data.height * H, H - y1))

            x1_text = x1
            y1_text = max(0, y1 - 10)

            img = cv2.putText(img, f"Score: {np.round(detection.score[0], 2) * 100}%", 
                              (x1_text, y1_text), cv2.FONT_HERSHEY_SIMPLEX, 
                              0.65, (0, 255, 0), 3)
            img = cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 6)
            if h > 0 and w > 0:
                img[y1:y1 + h, x1:x1 + w, :] = cv2.blur(img[y1:y1 + h, x1:x1 + w, :], (50, 50))

# parse arguments
parser = argparse.ArgumentParser()

parser.add_argument('--mode', default='image')
parser.add_argument('--filepath', default=os.path.join('.', 'data', 'face.jpg'))

args = parser.parse_args()

if args.mode == 'image':
    img = cv2.imread(args.filepath)
    img = cv2.resize(img, (800, 600))

    detector = mp.solutions.face_detection

    with detector.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detector:
        detect_faces(img, face_detector)

    if not os.path.exists('./data/output'):
        os.makedirs('./data/output')
    cv2.imwrite('./data/output/img_blur.jpg', img)

elif args.mode == 'video':
    detector = mp.solutions.face_detection
    video = cv2.VideoCapture(args.filepath)

    frame_width = int(video.get(3)) 
    frame_height = int(video.get(4)) 
   
    size = (frame_width, frame_height) 

    if not os.path.exists('./data/output'):
        os.makedirs('./data/output')

    result = cv2.VideoWriter('./data/ouput/filename.mp4',
                         cv2.VideoWriter_fourcc(*'mp4v'), 
                         10, size)
    
    while True:
        ret, frame = video.read()

        if not ret:
            break
        
        with detector.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detector:
            detect_faces(frame, face_detector)
        
        result.write(frame)

        if cv2.waitKey(10) & 0xFF == ord('s'): 
            break
    video.release()
    result.release()

    cv2.destroyAllWindows()

elif args.mode == 'webcam':
    video = cv2.VideoCapture(0)
    detector = mp.solutions.face_detection

    while True:
        ret, frame = video.read()
        if not ret:
            break
        with detector.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detector:
            detect_faces(frame, face_detector)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        cv2.imshow('Webcam', frame)
    video.release()
    cv2.destroyAllWindows()
