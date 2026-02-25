# Q2) Count Words in a File

# Problem Statement:
# Write a program which accepts a file name from the user and counts the total number of 
# words in that file.

# Input:
# Demo.txt

# Expected Output:
# Total number of words in Demo.txt.

import os

def FindNoLines(FileName):

    Count = 0

    if(os.path.exists(FileName)):

        fobj = open(FileName, "r")

        for line in fobj:
            List1 = line.split()
            Count = Count + len(List1)

    else:
        print("File does not exist")

    return Count

def main():
    Ret = 0

    FileName = input("Enter File Name : ")

    Ret = FindNoLines(FileName)

    print(f"Number of words in {FileName} is {Ret}")

if __name__ == "__main__":
    main()