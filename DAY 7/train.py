import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score





data_dict = pickle.load(open('DAY 7/data.pickle', 'rb'))


data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size = 0.2, shuffle = True, stratify = labels)




