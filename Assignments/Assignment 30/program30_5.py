# Q5) Search a Word in File

# Problem Statement:
# Write a program which accepts a file name and a word from the user and checks whether 
# that word is present in the file or not.

# Input:
# Demo.txt Marvellous

# Expected Output:
# Display whether the word Marvellous is found in Demo.txt or not.

import os

def FindNoLines(FileName, Word):
    bFlag = False

    if(os.path.exists(FileName)):

        fobj = open(FileName, "r")

        for line in fobj:
            List1 = line.split()

            for i in List1:
                if Word == i:
                    bFlag = True

    else:
        print("File does not exist")

    return bFlag

def main():
    Ret = False

    FileName = input("Enter File Name : ")
    Word = input("Enter word you want to find : ")

    Ret = FindNoLines(FileName, Word)

    if(Ret == True):
        print("The word exists")
    else:
        print("Word doesn't exist")


if __name__ == "__main__":
    main()