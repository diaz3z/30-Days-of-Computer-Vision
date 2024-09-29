import os
import mediapipe as mp
import numpy as np
import cv2
import pickle

DATA_DIR = "DAY 7/data"

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Initialize MediaPipe Hands for hand detection
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0)

data = []
labels = []

# Loop through each subdirectory (each sign) and images
for dir_ in os.listdir(DATA_DIR):
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
        data_aux = []
        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Process the image to detect hand landmarks
        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            # Only process the first hand detected
            hand_landmarks = results.multi_hand_landmarks[0]
            if len(hand_landmarks.landmark) == 21:  # One hand always has 21 landmarks
                for i in range(21):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x)
                    data_aux.append(y)

            # Only append data if 42 values (21 landmarks * 2) are collected
            if len(data_aux) == 42:
                data.append(data_aux)
                labels.append(dir_)

# Save the extracted data and labels in a pickle file
with open('data.pickle', 'wb') as f:
    pickle.dump({'data': data, 'labels': labels}, f)
