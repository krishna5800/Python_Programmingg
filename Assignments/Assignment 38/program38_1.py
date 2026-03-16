# 1. Write a Python program to load the file student_performance_ml.csv using pandas. 
# Display:
# • First 5 records
# • Last 5 records
# • Total number of rows and columns
# • List of column names
# • Data types of each column

import pandas as pd

def main():

    # Step 1 : Load the dataset

    df = pd.read_csv("student_performance_ml.csv")

    # EDA
    print("Few recored from top : (head)")
    print(df.head())

    print("\nFew records from bottom : (tail)")
    print(df.tail())

    print("\nTotal number of rows and columns : ")
    print(df.shape)

    print("\nData type of each column : ")
    for col in df.columns:
        print(col, " : ", df[col].dtype)

if __name__ == "__main__":
    main()