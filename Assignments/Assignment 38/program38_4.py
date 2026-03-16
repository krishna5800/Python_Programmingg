# 4. Use value_counts() to analyze the distribution of FinalResult. 
# Calculate the percentage of Pass and Fail students. 
# Is the dataset balanced? Justify your answer

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

if __name__ == "__main__":
    main()