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
    
    #---------------------------------------------------------------
    #   Step 4 : Use Elbow Methode
    #---------------------------------------------------------------

    print("\nStep 4 : Use Elbow Methode")

    WCSS = []

    for i in range(1,11):
        model = KMeans(n_clusters = i, random_state = 42, n_init = 5)
        model.fit(X_scaled)
        WCSS.append(model.inertia_)

    plt.figure(figsize = (8,5))

    plt.plot(range(1, 11), WCSS, marker = 'o')

    plt.xlabel("Number of Clusters")
    plt.ylabel("WCSS")
    plt.title("Elbow Methode")

    plt.grid(True)
    plt.show()

    #---------------------------------------------------------------
    #   Step 5 : Train the model
    #---------------------------------------------------------------

    print("\nStep 5 : Train the model")

    model = KMeans(n_clusters = 4, random_state = 42, n_init = 10)

    clusters = model.fit_predict(X_scaled)

    df["clusters"] = clusters

    print("\nDataset with clusters : ")
    print(df.head())


if __name__ == "__main__":
    main()