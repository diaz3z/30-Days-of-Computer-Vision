from utils import get_face_landmarks
import os
import cv2
import numpy as np

data_dir = "DAY 6\data"

output = []

for emotion_indx, emotion in enumerate(os.listdir(data_dir)):
    for image_path in os.listdir(os.path.join(data_dir, emotion)):
        image_path = os.path.join(data_dir, emotion, image_path)

        image = cv2.imread(image_path)

        face_landmarks = get_face_landmarks(image)

        if len(face_landmarks) == 1404:
            face_landmarks.append(int(emotion_indx))
            output.append(face_landmarks)
            
np.savetxt(os.path.join(os.path.dirname(__file__), "data.txt"), np.asarray(output))
