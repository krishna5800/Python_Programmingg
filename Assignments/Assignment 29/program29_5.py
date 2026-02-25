# Q5) Frequency of a String in File

# Problem Statement:

# Write a program which accepts a file name and one string from the user and 
# returns the frequency (count of occurrences) of that string in the file.

# Input:
# Demo.txt Marvellous

# Expected Output:
# Count how many times "Marvellous" appears in Demo.txt.

import os
import sys
import hashlib

def FindCount(FileName, Target):

    Count = 0

    fobj = open(FileName, "r")
    
    Buffer = fobj.read()

    Split = Buffer.split()

    for i in Split:
        if Target == i:
            Count = Count + 1

    return Count


def main():

    if (len(sys.argv) != 3):
        print("Invalid Arguments")
        return

    Ret = FindCount(sys.argv[1], sys.argv[2])  # Demo.txt Marvellous

    print(Ret)

if __name__  == "__main__":
    main()