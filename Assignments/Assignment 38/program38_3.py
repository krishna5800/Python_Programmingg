# 3. Using pandas functions, calculate and display:
# • Average StudyHours
# • Average Attendance
# • Maximum PreviousScore
# • Minimum SleepHours

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

if __name__ == "__main__":
    main()