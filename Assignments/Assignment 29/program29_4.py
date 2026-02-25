# Q4) Compare Two Files (Command Line)

# Problem Statement:

# Write a program which accepts two file names through command line arguments 
# and compares the contents of both files.

# If both files contain the same contents, display Success
# Otherwise display Failure

# Input (Command Line):
# Demo.txt Hello.txt

# Expected Output:
# Success OR Failure

import os
import sys
import hashlib

def CalculateChecksum(FileName):

    hobj = hashlib.md5()

    fobj = open(FileName, "rb")
    Buffer = fobj.read()

    hobj.update(Buffer)

    return hobj.hexdigest()

def CompFileContent(FileName1, FileName2):
    Ret = False

    Checksum1 = CalculateChecksum(FileName1)

    Checksum2 = CalculateChecksum(FileName2)

    if Checksum1 == Checksum2:
        return True
    else:
        return False

def main():

    if (len(sys.argv) != 3):
        print("Invalid Arguments")
        return

    Ret = CompFileContent(sys.argv[1], sys.argv[2])  # ABC.txt Demo.txt

    if Ret == True:
        print("Same Content")
    else:
        print("Not Same Content")

if __name__  == "__main__":
    main()