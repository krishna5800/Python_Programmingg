import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

#----------------------------------------------------------
# Step 1 : Load the dataset
#----------------------------------------------------------

df = pd.read_csv("Breast_cancer.csv")

print("Shape of dataset : ", df.shape)

print("\nFirst 5 records from dataset : ")
print(df.head())

#----------------------------------------------------------
# Step 2 : Separate features and lables
#----------------------------------------------------------

X = df.drop("target", axis = 1)
Y = df["target"]

#----------------------------------------------------------
# Step 3 : Split the datset for training and testing
#----------------------------------------------------------

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state = 42, test_size = 0.20)

#----------------------------------------------------------
# Step 4 : Create the base model
#----------------------------------------------------------

base_model = DecisionTreeClassifier(random_state = 42)

#----------------------------------------------------------
# Step 5 : Create Bagging Model
#----------------------------------------------------------

bagging_model = BaggingClassifier(
                estimator = base_model, 
                n_estimators = 10,
                random_state = 42
                )

#----------------------------------------------------------
# Step 6 : Train Bagging Model
#----------------------------------------------------------

bagging_model.fit(X_train, Y_train)

#----------------------------------------------------------
# Step 7 : Test Bagging Model
#----------------------------------------------------------

Y_Pred = bagging_model.predict(X_test)

#----------------------------------------------------------
# Step 8 : Evaluate Bagging Model
#----------------------------------------------------------

print("\nBagging Accuracy : ", accuracy_score(Y_test, Y_Pred) * 100)

print("\nConfusion Matrix : ")
print(confusion_matrix(Y_test, Y_Pred))