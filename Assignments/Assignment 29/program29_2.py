# Q2) Display File Contents

# Problem Statement:

# Write a program which accepts a file name from the user, opens that file, 
# and displays the entire contents on the console.

# Input:
# Demo.txt

# Expected Output:
# Display contents of Demo. txt, on console.

import os

def DisplayFileContents(FileName):
    Ret = False

    fobj = open(FileName, "r")

    Ret = os.path.exists(FileName)

    if Ret == False:
        print("Their is no such file in current directroy")
        return
    
    print(fobj.read())

def main():
    
    FileName = input("Enter Name : ")
    DisplayFileContents(FileName)

if __name__  == "__main__":
    main()