import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv('data/merged_5s.csv', sep=",")

data.drop(columns=['Source IP', ' Source Port', ' Destination IP', ' Destination Port', ' Protocol'], inplace=True)
data.replace({'label': {'TOR': 1, 'nonTOR': 0}}, inplace=True)

y = data['label']
X = data.drop(columns=['label'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, shuffle=True, stratify=y)

X_train = np.nan_to_num(X_train)
X_test = np.nan_to_num(X_test)

knn = KNeighborsClassifier(n_neighbors=5, p=2, metric='minkowski')

knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

print(accuracy_score(y_test, y_pred))
