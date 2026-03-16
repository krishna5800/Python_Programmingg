# 8. Draw a boxplot for Attendance. 
# Identify if any outliers are present.

import pandas as pd
import matplotlib.pyplot as plt

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

    print("\nTotal number of students in dataset : ")
    print(df["StudyHours"].count())

    print("\nStudents passed : ")
    print((df["FinalResult"] == 1).sum())

    print("\nStudents failed : ")
    print((df["FinalResult"] == 0).sum())

    print("\nAverage Study Hours : ")
    print(df["StudyHours"].mean())

    print("\nAverage Attendance : ")
    print(df["Attendance"].mean())

    print("\nMaximum previous score : ")
    print(df["PreviousScore"].max())

    print("\nMinimum Sleep hours : ")
    print(df["SleepHours"].min())

    print("\nValue_counts() to analyze the distribution of FinalResult")
    print(df["FinalResult"].value_counts)

    print("\nCalculate the percentage of Pass and Fail students : ")

    print("\nPercentage of students passed : ")

    passed = (df["FinalResult"] == 1).sum()
    total = df["FinalResult"].count()

    percent = (passed/total) * 100

    print("Percentage of passe students : ", percent,"%")

    print("\nPercentage of students failed : ")

    failed = (df["FinalResult"] == 0).sum()
    total = df["FinalResult"].count()

    percent = (failed/total) * 100

    print("Percentage of passe students : ", percent,"%")

    '''
    # • Higher StudyHours increase the chance of passing.  -->> Yes it's true
    # • Higher Attendance improves FinalResult.            -->> Yes it's true

    for this i have used visualization
    '''

    # 1
    plt.figure(figsize = (5,5))
    plt.title("Study Hours VS Final Result")

    plt.scatter(df["StudyHours"], df["FinalResult"])

    plt.xlabel("StudyHours")
    plt.ylabel("FinalResult ")
    plt.grid(True)
    plt.show()

    # 2
    plt.figure(figsize = (5,5))
    plt.title("Attendance VS Final Result")

    plt.scatter(df["Attendance"], df["FinalResult"])

    plt.xlabel("Attendance")
    plt.ylabel("FinalResult ")
    plt.grid(True)
    plt.show()

    print("\nHistogram of Study Hours : ")

    plt.figure(figsize = (8,5))
    plt.title("Histogram of Study Hours")

    plt.hist(df["StudyHours"])

    plt.xlabel("StudyHours")
    plt.grid(True)
    plt.show()

    print("\nScatter plot of : StudyHours vs PreviousScore")

    plt.figure(figsize = (8,5))
    plt.title("StudyHours vs PreviousScore")

    plt.scatter(df["SleepHours"], df["PreviousScore"])

    plt.xlabel("StudyHours")
    plt.ylabel("PreviousScore")
    plt.grid(True)
    plt.show()

    print("\nDraw a boxplot for Attendance")

    plt.figure(figsize = (8,5))
    plt.title("Box plot of Attendence")

    plt.boxplot(df["Attendance"])

    plt.xlabel("Attendance")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()