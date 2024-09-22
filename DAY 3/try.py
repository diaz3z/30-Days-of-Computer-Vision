import cv2
import mediapipe as mp
import numpy as np

mp_face_detection = mp.solutions.face_detection
mp_face_detection = mp_face_detection.FaceDetection()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = mp_face_detection.process(frame_rgb)
    if results.detections:
        for detection in results.detections:
            bbox = detection.location_data.relative_bounding_box
            ih, iw, _ = frame.shape
            x, y, w, h = int(bbox.xmin * iw), int(bbox.ymin * ih), int(bbox.width * iw), int(bbox.height * ih)

            mask = np.zeros_like(frame, dtype=np.uint8)
            center = (x + w // 2, y + h // 2)
            axes = (w // 2, h // 2)
            angle = 0

            bound = cv2.rectangle(mask, (x, y), (x+w, y+h), (0, 255, 0), 2)
            blurred_frame = cv2.GaussianBlur(bound, (99, 99), 30)
            frame = np.where(mask == 255, blurred_frame, frame)
    cv2.imshow("fasdf", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()