import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.face_detection
mp_face_detection = mp_face_detection.FaceDetection()


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = mp_face_detection.process(frame_rgb)

    if results.detections:
        for detection in results.detections:
            bboxC =detection.location_data.relative_bounding_box
            ih, iw, _ = frame.shape
            x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)

            bounding = cv2.rectangle(frame, (x, y), (x + w, y + h),(0,255,0), 2)
            blur = cv2.GaussianBlur(bounding, (99,99), 0)

    cv2.imshow("Face", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()