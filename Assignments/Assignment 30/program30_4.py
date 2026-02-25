# Q4) Copy File Contents into Another File

# Problem Statement:
# Write a program which accepts two file names from the user.
# • First file is an existing file
# • Second file is a new file
# Copy all contents from the first file into the second file.

# Input:
# ABC.txt Demo.txt

# Expected Output:
# Contents of ABC.txt copied into Demo.txt.

import os

def FindNoLines(FileSrc, FileDest):

    if(os.path.exists(FileSrc)):

        fsrc = open(FileSrc, "r")
        fdest = open(FileDest, "w")

        for line in fsrc:
            fdest.write(line)

    else:
        print("File does not exist")

    print("File Copied Successfully")

def main():
    Ret = 0

    FileSrc = input("Enter Source File Name : ")

    FileDest = input("Enter Destination File Name : ")

    FindNoLines(FileSrc, FileDest)


if __name__ == "__main__":
    main()