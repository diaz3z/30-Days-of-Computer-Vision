import cv2
import util

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    hsvImg = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mask = cv2.inRange(hsvImg, ())

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()