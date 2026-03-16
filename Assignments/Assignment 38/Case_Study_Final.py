import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("student_performance_ml.csv")

print("Few Records : ")
print(df.head())

print("\nShape of dataset : ", df.shape)

print("\nAre any NULL values : ")
print(df.isnull().sum())

X = df[["StudyHours","Attendance","PreviousScore","AssignmentsCompleted", "SleepHours"]]
Y = df["FinalResult"]

print("\nShape of Independent features : ", X.shape)
print("\nShape of Dependent features : ", Y.shape)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state = 42, test_size = 0.20)

print("\nShape of X_train : ", X_train.shape)
print("\nShape of X_test : ", X_test.shape)
print("\nShape of Y_train : ", Y_train.shape)
print("\nShape of Y_test : ", Y_test.shape)

model = DecisionTreeClassifier()

model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

Accuracy = accuracy_score(Y_test, Y_pred)

print("\nAccuracy of model is : ", Accuracy*100)