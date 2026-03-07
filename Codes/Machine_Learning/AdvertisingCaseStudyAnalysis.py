import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

def MarvellousAdvertise(DataPath):

    Border = "-"*55

    #----------------------------------------------------
    # Step 1 : Load Dataset
    #----------------------------------------------------

    print(Border)
    print("Step 1 : Load Dataset")
    print(Border)

    df = pd.read_csv(DataPath)

    print("Few records from dataset : ")
    print(Border)
    print(df.head())

    #----------------------------------------------------
    # Step 2 : Data Cleaning (Remove Unwanted Columns)
    #----------------------------------------------------

    print(Border)
    print("Step 2 : Data Cleaning (Remove Unwanted Columns)")
    print(Border)

    print("Shape of dataset before removal : ", df.shape)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns = 'Unnamed: 0',inplace = True)

    print("Shape of dataset after removal : ", df.shape)

    print(Border)
    print("Clean dataset is : ")
    print(Border)

    print(df.head())

    #----------------------------------------------------
    # Step 3 : Check Missing Values
    #----------------------------------------------------

    print(Border)
    print("Step 3 : Check Missing Values")
    print(Border)

    print("Missing values count : ")
    print(df.isnull().sum())

    #----------------------------------------------------
    # Step 4 : Display Statistical Summary
    #----------------------------------------------------

    print(Border)
    print("Step 4 : Display Statistical Summary")
    print(Border)

    print(df.describe())

    #----------------------------------------------------
    # Step 5 : Display Correlation Between Columns
    #----------------------------------------------------

    print(Border)
    print("Step 5 : Display Correlation Between Columns")
    print(Border)

    print("Correlation Matrix : ")
    print(Border)
    
    print(df.corr())

def main():
    MarvellousAdvertise("Advertising.csv")

if __name__ == "__main__":
    main()