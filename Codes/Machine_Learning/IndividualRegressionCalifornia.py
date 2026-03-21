import pandas as pd
 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

#----------------------------------------------------------
# Step 1 : Load the dataset
#----------------------------------------------------------

df = pd.read_csv("california_housing.csv")

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

dt_model = DecisionTreeRegressor(random_state = 42)

#----------------------------------------------------------
# Step 5 : Train Model
#----------------------------------------------------------

dt_model.fit(X_train, Y_train)

#----------------------------------------------------------
# Step 6 : Test Model
#----------------------------------------------------------

Y_Pred = dt_model.predict(X_test)

#----------------------------------------------------------
# Step 7 : Evaluate Model
#----------------------------------------------------------

print("\nMean Squared Error : ", mean_squared_error(Y_test, Y_Pred))

print("\nR2 Score : ", r2_score(Y_test, Y_Pred))