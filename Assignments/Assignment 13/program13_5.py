# 5. Write a program which accepts marks and displays grade.

# Condition Example:
# 75-Distinction
# 60 First Class
# 50 Second Class
# <50+Fail

def DisplayGrades(No):

    if(No < 50 and No >= 0):
        print("Fail :(")
    elif(No >= 50 and No < 60):
        print("Second Class")
    elif(No >= 60 and No < 75):
        print("First Class")
    elif(No >= 75 and No <= 100):
        print("Distinction")
    else:
        print("Invalid Marks")

def main():
    Marks = 0

    Marks = int(input("Enter your marks : "))

    DisplayGrades(Marks)

if __name__ == "__main__":
    main()