# 3. Design automation script which accept directory name and delete all duplicate files 
# from that directory. Write names of duplicate files from that directory into log file named 
# as Log.txt. Log.txt file should be created into current directory.

# Usage : DirectoryDusplicateRemoval.py “Demo”
# Demo is name of directory.

import sys
import DirectoryDusplicateRemoval

def main():
    DirName = sys.argv[1]

    DirectoryDusplicateRemoval.DirectoryDuplicateRemoval(DirName)

if __name__ == "__main__":
    main()