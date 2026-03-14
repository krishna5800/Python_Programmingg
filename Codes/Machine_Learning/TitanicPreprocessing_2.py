import pandas as pd
import numpy as np
import joblib

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
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

    return df

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