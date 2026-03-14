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