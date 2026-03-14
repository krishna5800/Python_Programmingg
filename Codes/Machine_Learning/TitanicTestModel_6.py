import pandas as pd
import numpy as np
import joblib

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.linear_model import LogisticRegression

#---------------------------------------------------------------
#
#   Function Name : DisplayInfo
#   Description :   It displays the formated title
#   Parameters :    Title (Str)
#   Return :        None
#   Date :          14/03/2026
#   Author :        Krishna Govindrav Hitnalikar
#
#---------------------------------------------------------------

def DisplayInfo(title):
    print("\n" + "="*82)
    print(title)
    print("="*82)

#---------------------------------------------------------------
#
#   Function Name : ShowData
#   Description :   It shows basic infromation about dataset
#   Parameters :    Dataset (df)
#                   df --> Pandas data frame object
#                   Message
#                   message --> Heading text to display
#   Return :        None
#   Date :          14/03/2026
#   Author :        Krishna Govindrav Hitnalikar
#
#---------------------------------------------------------------

def ShowData(df, message):
    DisplayInfo(message)

    print("\nFirst 5 rows of dataset")
    print(df.head())

    print("\nShape of dataset")
    print(df.shape)

    print("\nColumn names : ")
    print(df.columns.tolist())

    print("\nMissing values in each cloumns")
    print(df.isnull().sum())

#---------------------------------------------------------------
#
#   Function Name : CleanTitanicData
#   Description :   It does preprocessing
#                   It removes unnecessary columns
#                   It handles missing values
#                   It converts text data to numeric format
#                   It does encoding of categorical columns
#   Parameters :    Dataset (df)
#                   df --> Pandas data frame object
#   Return :        Dataset (df)
#                   df --> Cleaned pandas data frame object
#   Date :          14/03/2026
#   Author :        Krishna Govindrav Hitnalikar
#
#---------------------------------------------------------------

def CleanTitanicData(df):
    DisplayInfo("Step 2 : Original Data")
    print(df.head())
    print("Shape : ", df.shape)

    # Remove unecessary columns
    drop_columns = ["Passengerid", "zero", "Name", "Cabin"]
    existing_columns = [col for col in drop_columns if col in df.columns]

    print("\nColumns to be droped : ")
    print(existing_columns)

    # Drop the unwanted columns
    df = df.drop(columns = existing_columns)

    DisplayInfo("Step 2 : Data after column removal")
    print(df.head())
    print("Shape : ", df.shape)

    # Handle age column
    if "Age" in df.columns:
        print("\nAge column before filling missing values : ")
        print(df["Age"].head(10))

        # coerce -> Invalid value gets converted into NaN
        df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

        age_median = df["Age"].median()
        print("\nMedian of Age column : ", age_median)

        # Replace missing values with median
        df["Age"] = df["Age"].fillna(age_median)

        print("\nAge column after preprocessing : ")
        print(df["Age"].head(10))

    # Handle Fare column
    if "Fare" in df.columns:
        print("\nFare column before preprocessing : ")
        print(df["Fare"].head(10))

        # coerce -> Invalid value gets converted into NaN
        df["Fare"] = pd.to_numeric(df["Fare"], errors="coerce")

        fare_median = df["Fare"].median()
        print("\nMedian of Fare column : ", fare_median)

        # Replace missing values with median
        df["Fare"] = df["Fare"].fillna(fare_median)

        print("\nFare column after preprocessing : ")
        print(df["Fare"].head(10))

    # Handling Embarked column
    if "Embarked" in df.columns:
        print("\nEmbarked before preprocessing")
        print(df["Embarked"].head(10))

        # Convert the data into the string
        df["Embarked"] = df["Embarked"].astype(str).str.strip()

        # Remove missing values
        df["Embarked"] = df["Embarked"].replace(['nan', 'None', ''], np.nan)

        # Get most frequent value
        embarked_mode = df["Embarked"].mode()[0]
        print("\nMode of embarked column : ", embarked_mode)
        
        df["Embarked"] = df["Embarked"].fillna(embarked_mode)

        print("\nEmbarked after preprocessing : ")
        print(df["Embarked"].head(10))

    # Handle Sex Column
    if "Sex" in df.columns:
        print("\nSex column before preprocessing : ")
        print(df["Sex"].head(10))

        # coerce -> Invalid value gets converted into NaN
        df["Sex"] = pd.to_numeric(df["Sex"], errors="coerce")

        print("\nSex column after preprocessing : ")
        print(df["Sex"].head(10))

    DisplayInfo("Display data after preprocessing")
    print(df.head())

    print("Missing values after preprocessing")
    print(df.isnull().sum())

    # Encode Embarked Column
    df = pd.get_dummies(df, columns = ["Embarked"], drop_first=True)
    print("\nData after encoding")

    print(df.head())
    print("Shape of dataset : ",df.shape)

    # Convert boolean columns into integer
    for col in df.columns:
        if df[col].dtype == bool:
            df[col] = df[col].astype(int)

    print("\nData after encoding")

    print(df.head())
    print("Shape of dataset : ",df.shape)

    return df

#---------------------------------------------------------------
#
#   Function Name : TrainTitanicModel
#   Description :   It does split X, Y, training data, testing data
#   Parameters :    Dataframe(df)
#   Return :        None
#   Date :          14/03/2026
#   Author :        Krishna Govindrav Hitnalikar
#
#---------------------------------------------------------------

def TrainTitanicModel(df):

    # Split features and lables
    X = df.drop("Survived", axis = 1)
    Y = df["Survived"]

    print("\nFeatures : ")
    print(X.head())

    print("\nLables : ")
    print(Y.head())

    print("Shape of X : ", X.shape)
    print("Shape of Y : ", Y.shape)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.20, random_state = 42)

    print("Shape of X_train : ", X_train.shape)
    print("Shape of X_test : ", X_test.shape)
    print("Shape of Y_train : ", Y_train.shape)
    print("Shape of Y_test : ", Y_test.shape)

    model = LogisticRegression(max_iter = 1000)

    model.fit(X_train, Y_train)

    print("Model trained Successfully")

    print("\nIntercept of model : ")
    print(model.intercept_)

    print("\nCoefficient of model : ")
    for feature, coef in zip(X.columns, model.coef_[0]):
        print(feature, " : ", coef)

    PreserveModel(model, "MarvellousTitanic.pkl")

    loaded_model = LoadPreservedModel("MarvellousTitanic.pkl")

    Y_Pred = loaded_model.predict(X_test)

    Accuracy = accuracy_score(Y_Pred, Y_test)

    print("Accuracy is : ", Accuracy*100)

    cm = confusion_matrix(Y_Pred, Y_test)

    print("Confusion matrix is : ")
    print(cm)

#---------------------------------------------------------------
#
#   Function Name : PreserveModel
#   Description :   It is used to preserve model on secondary
#   Parameters :    Model, File Name
#   Return :        None
#   Date :          14/03/2026
#   Author :        Krishna Govindrav Hitnalikar
#
#---------------------------------------------------------------

def PreserveModel(model, FileName):
    joblib.dump(model, filename= FileName)

    print("Model preserved successfully with name : ", FileName)

#---------------------------------------------------------------
#
#   Function Name : LoadPreservedModel
#   Description :   It is used to load preserved model
#   Parameters :    FileName
#   Return :        model
#   Date :          14/03/2026
#   Author :        Krishna Govindrav Hitnalikar
#
#---------------------------------------------------------------

def LoadPreservedModel(FileName):

    loaded_model = joblib.load(filename=FileName)

    print("Model Successfuly loaded")

    return loaded_model

#---------------------------------------------------------------
#
#   Function Name : MarvellousTitanicLogistic
#   Description :   This is main pipeline controller
#                   It loads the dataset, shows raw data
#                   It preprocess the dataset & train the model
#   Parameters :    Data path of the dataset file
#   Return :        None
#   Date :          14/03/2026
#   Author :        Krishna Govindrav Hitnalikar
#
#---------------------------------------------------------------

def MarvellousTitanicLogistic(DataPath):

    DisplayInfo("Step 1 : Loading the dataset")
    df = pd.read_csv(DataPath)

    ShowData(df, "Initial Dataset")

    df = CleanTitanicData(df)

    TrainTitanicModel(df)

#---------------------------------------------------------------
#
#   Function Name : main
#   Description :   Starting point of the application
#   Parameters :    None
#   Return :        None
#   Date :          14/03/2026
#   Author :        Krishna Govindrav Hitnalikar
#
#---------------------------------------------------------------

def main():
    MarvellousTitanicLogistic("TitanicDataset.csv")

if __name__ == "__main__":
    main()