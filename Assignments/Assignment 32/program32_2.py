# 2. Design automation script which accept directory name and write names of duplicate files 
# from that directory into log file named as Log.txt. Log.txt file should be created into 
# current directory.

# Usage : DirectoryDuplicate.py “Demo”
# Demo is name of directory.

import sys
import DirectoryDuplicate

def main():
    DirName = sys.argv[1]

    DirectoryDuplicate.DirectoryDuplicate(DirName)

if __name__ == "__main__":
    main()