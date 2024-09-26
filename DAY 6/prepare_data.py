from utils import get_face_landmarks
import os
import cv2


data_dir = "./data"

for emotion in os.listdir(data_dir):
    for image_path in os.listdir(os.path.join(data_dir, emotion)):
        image_path = os.path.join(data_dir, emotion, image_path)

        image_rows, image_cols, _ = 