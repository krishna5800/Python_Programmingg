# Q3) Copy File Contents into a New File (Command Line)

# Problem Statement:

# Write a program which accepts an existing tile name through command line arguments, 
# creates a new file named Demo.txt, and copies all contents from the given file into Demo. txt.

# Input (Command Line):
# ABC.txt

# Expected Output:
# Create Demo.txt and copy contents of ABC.txt into Demo.txt.

import os
import sys

def CopyFileContents(FileName):
    Ret = False

    fobj1 = open(FileName, "r")

    Ret = os.path.exists(FileName)

    if Ret == False:
        print("Their is no such file")
        return
    
    fobj2 = open("Demo.txt", "w")

    Buffer = fobj1.read()
    fobj2.write(Buffer)
    print("Data Copied Successfully")

def main():

    if (len(sys.argv) != 2):
        print("Invalid Arguments")
        return

    CopyFileContents(sys.argv[1])  # ABC.txt

if __name__  == "__main__":
    main()