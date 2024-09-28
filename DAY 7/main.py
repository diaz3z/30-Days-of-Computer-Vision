import cv2
from cvzone.HandTrackingModule import HandDetector


cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

while True:
    ret, frame =  cap.read()
    hands, frame = detector.findHands(frame)
    cv2.imshow("frame", frame)
    cv2.waitKey(1)