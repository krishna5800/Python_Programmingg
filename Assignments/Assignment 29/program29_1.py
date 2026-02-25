# Q1) Check File Exists in Current Directory

# Problem Statement:

# Write a program which accepts a file name from the user and checks whether that file 
# exists in the current directory or not.

# Input:
# Demo.txt

# Expected Output:
# Display whether Demo.txt exists or not.

import os

def ChkFileExist(FileName):
    Ret = False

    Ret = os.path.exists(FileName)

    return Ret

def main():
    
    FileName = input("Enter Name : ")
    Ans = ChkFileExist(FileName)

    if Ans == True:
        print("File exists in current directory")
    else:
        print("Their is no such file in current directroy")

if __name__  == "__main__":
    main()