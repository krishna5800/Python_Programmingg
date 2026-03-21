import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
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
# Step 4 : Create model
#----------------------------------------------------------

dt_model = DecisionTreeClassifier(random_state = 42)

#----------------------------------------------------------
# Step 5 : Train Decision Tree Model
#----------------------------------------------------------

dt_model.fit(X_train, Y_train)

#----------------------------------------------------------
# Step 6 : Test Decision Tree Model
#----------------------------------------------------------

Y_Pred = dt_model.predict(X_test)

#----------------------------------------------------------
# Step 7 : Evaluate Decision Tree Model
#----------------------------------------------------------

print("\nAccuracy : ", accuracy_score(Y_test, Y_Pred) * 100)

print("\nConfusion Matrix : ")
print(confusion_matrix(Y_test, Y_Pred))