import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

data = {'StudyHours': [2, 4, 6, 8, 10],
        'Attendance': [50, 60, 70, 80, 90],
        'Result': [0, 0, 1, 1, 1]
        }

df = pd.DataFrame(data)
print("Original Data:")
print(df)
X = df[["StudyHours", "Attendance"]]
y = df["Result"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", model.score(X_test, y_test))

new_student = np.array([[5, 65]])
prediction = model.predict(new_student)
print("prediction for new student:", prediction)

