# Q1) Count Lines in a File

# Problem Statement:
# Write a program which accepts a file name from the user and counts how many lines are 
# present in the file.

# Input:
# Demo.txt

# Expected Output:
# Total number of lines in Demo.txt.

import os

def FindNoLines(FileName):

    iCount = 0

    if(os.path.exists(FileName)):

        fobj = open(FileName, "r")

        for line in fobj:
            iCount = iCount + 1
        
    else:
        print("File does not exist")

    return iCount

def main():
    Ret = 0

    FileName = input("Enter File Name : ")

    Ret = FindNoLines(FileName)

    print(f"Number of lines in {FileName} is {Ret}")

if __name__ == "__main__":
    main()