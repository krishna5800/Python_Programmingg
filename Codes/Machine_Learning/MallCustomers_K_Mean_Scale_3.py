import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def main():
    
    #---------------------------------------------------------------
    #   Step 1 : Load Dataset
    #---------------------------------------------------------------

    print("Step 1 : Load Dataset")

    df = pd.read_csv("Mall_Customers.csv")

    print("\nFirst Few Records : ")
    print(df.head())

    print("\nShape of Dataset : ")
    print(df.shape)

    print("\nMissing Values :")
    print(df.isnull().sum())

    #---------------------------------------------------------------
    #   Step 2 : Select Features (Independent)
    #---------------------------------------------------------------

    print("\nStep 2 : Select Features (Independent)")

    X = df[["AnnualIncome", "SpendingScore"]]

    print("\nSelected features : ")
    print(X.head())

    print("\nShape of selected features : ")
    print(X.shape)

    #---------------------------------------------------------------
    #   Step 3 : Scale the data
    #---------------------------------------------------------------

    print("\nStep 3 : Scale the data")

    scalar = StandardScaler()
    X_scaled = scalar.fit_transform(X)
    
    print("\nData after scaling : ")
    print(X_scaled[:5])

if __name__ == "__main__":
    main()