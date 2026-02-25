# Q3) Display File Line by Line

# Problem Statement:
# Write a program which accepts a file name from the user and displays the contents of 
# the file line by line on the screen.

# Input:
# Demo.txt

# Expected Output:
# Display each line of Demo.txt one by one.

import os

def FindNoLines(FileName):

    Count = 0

    if(os.path.exists(FileName)):

        fobj = open(FileName, "r")

        for line in fobj:
            print(line)

    else:
        print("File does not exist")

def main():
    Ret = 0

    FileName = input("Enter File Name : ")

    FindNoLines(FileName)


if __name__ == "__main__":
    main()