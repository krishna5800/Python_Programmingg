import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

from sklearn.preprocessing import StandardScaler

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

    # Step 4 : Split the dataset for training and testing

    print(Border)
    print("Step 4 : Split the dataset for training and testing")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state = 42, test_size = 0.20, stratify = Y)

    print(Border)
    print("Information of training data : ")
    print(Border)

    print("Shape of X_train : ",X_train.shape)
    print("Shape of X_test : ",X_test.shape)
    print("Shape of Y_train : ",Y_train.shape)
    print("Shape of Y_test : ",Y_test.shape)

    # Step 5 : Feature Scaling

    print(Border)
    print("Step 5 : Feature Scaling")
    print(Border)

    Scaler = StandardScaler()

    # Independent Variables Scaling

    X_train_Scaled = Scaler.fit_transform(X_train)
    X_test_Scaled = Scaler.fit_transform(X_test)

    print("Feature scaling is done")

    # Step 6 : Explore the multiple values of K
    # HYPER-PARAMETER TUNING(K)

    print(Border)
    print("Step 6 : Explore the multiple values of K (Hyper Parameter Tuning)")
    print(Border)

    accuracy_scores = []
    K_Values = range(1, 21)

    for k in K_Values:
        model = KNeighborsClassifier(n_neighbors = k)

        model.fit(X_train_Scaled, Y_train)
        Y_pred = model.predict(X_test_Scaled)

        Accuracy = accuracy_score(Y_test, Y_pred)

        accuracy_scores.append(Accuracy)

    print(Border)
    print("Accuracy report of all K values from 1 to 20")
    print(Border)
    
    for value in accuracy_scores:
        print(value)
    
    # Step 7 : Plot graph of K vs Accuracy

    print(Border)
    print("Step 7 : Plot graph of K vs Accuracy")
    print(Border)

    plt.figure(figsize=(8,5))

    plt.plot(K_Values, accuracy_scores, marker = 'o')

    plt.xlabel("Value of K")
    plt.ylabel("Accuracy")
    plt.title("K Values VS Accuracy")

    plt.xticks(list(K_Values))
    plt.grid(True)

    plt.show()

    # Step 8 : Find Best Value of K

    print(Border)
    print("Step 8 : Find Best Value of K")
    print(Border)

    best_K = list(K_Values)[accuracy_scores.index(max(accuracy_scores))]

    print("Best value of K is : ", best_K)

    # Step 9 : Build Final model usinf best value of K

    print(Border)
    print("Step 9 : Build Final model usinf best value of K")
    print(Border) 

    final_model = KNeighborsClassifier(n_neighbors = best_K)

    final_model.fit(X_train_Scaled, Y_train)

    Y_pred = final_model.predict(X_test_Scaled)

    # Step 10 : Calculate final accuracy

    print(Border)
    print("Step 10 : Calculate final accuracy")
    print(Border) 

    Accuracy = accuracy_score(Y_test, Y_pred)

    print("Accuracy of model is : ", Accuracy*100)

    # Step 11 : Display Confusion Matrix

    print(Border)
    print("Step 11 : Display Confusion Matrix")
    print(Border)

    CM = confusion_matrix(Y_test, Y_pred)

    print(Border)
    print("Confusion Matrix : ")
    print(Border)

    print(CM)

    # Step 12 : Display Classification report

    print(Border)
    print("Step 12 : Display Classification report")
    print(Border)

    print(Border)
    print("Classification Report")
    print(Border)

    print(classification_report(Y_test, Y_pred))

def main():
    Border = "-"*40

    print(Border)
    print("Wine Classifier using KNN")
    print(Border)

    MarvellousClassifier("WinePredictor.csv")

if __name__ == "__main__":
    main()