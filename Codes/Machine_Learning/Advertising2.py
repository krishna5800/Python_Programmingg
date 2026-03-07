import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def main():
    df = pd.read_csv("Advertising.csv")

    print(df.shape)

    # Data Cleaning

    if 'Unnamed: 0' in df.columns:
        df.drop(columns = ['Unnamed: 0'], inplace = True)

    print(df.shape)

    # Split the data into X and Y

    X = df[['TV', 'radio', 'newspaper']]
    Y = df['sales']

    print("Independent Variables : ", X.shape)
    print("Dependent Variables : ", Y.shape)

    # Split the data for training and tesing

    X_train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, random_state = 42, test_size = 0.10)

    model = LinearRegression()

    model.fit(X_train, Y_Train)

    Y_Pred = model.predict(X_Test)

    print("Testing data : ")
    print(X_Test)

    print("Predicted Values : ")
    print(Y_Pred)

    print("Actual Values : ")
    print(Y_Test)

    print("Coefficient : ", model.coef_)
    print("Intercept : ", model.intercept_)

if __name__ == "__main__":
    main()