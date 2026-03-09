import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

import matplotlib.pyplot as plt

def MarvellousClassifier(DataPath):
    Border = "-"*50

    # Step 1 : Load the Dataset from csv file

    print(Border)
    print("Step 1 : Load the Dataset from csv file")
    print(Border)

    df = pd.read_csv(DataPath)

    print(Border)
    print("Few records from dataset : ")
    print(Border)

    print(df.head())

    # Step 2 : Clean the dataset by removing empty sets

    print(Border)
    print("Step 2 : Clean the dataset by removing empty rows")
    print(Border)

    df.dropna(inplace=True)

    print("Total records : ", df.shape[0])
    print("Total columns : ", df.shape[1])

    # Step 3 : Separate independent and dependent variables

    print(Border)
    print("Step 3 : Separate independent and dependent variables")
    print(Border)

    # X = df[['Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline']]
    # OR

    X = df.drop(columns = ['Class'])
    Y = df['Class']

    print("Shape of X : ", X.shape)
    print("Shape of Y : ", Y.shape)

    print(Border)
    print("Input Columns : ", X.columns.tolist())
    print("Output Column : Class")

def main():
    Border = "-"*40

    print(Border)
    print("Wine Classifier using KNN")
    print(Border)

    MarvellousClassifier("WinePredictor.csv")


if __name__ == "__main__":
    main()