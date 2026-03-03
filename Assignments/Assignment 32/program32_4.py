# 4. Design automation script which accept directory name and delete all duplicate files from that
# directory. Write names of duplicate files from that directory into log file named as Log.txt.
# Log.txt file should be created into current directory. Display execution time required for the
# script.

# Usage : DirectoryDusplicateRemoval.py “Demo”
# Demo is name of directory.

import sys
import time
import DirectoryDusplicateRemoval

def main():
    DirName = sys.argv[1]

    start_time = time.time()

    DirectoryDusplicateRemoval.DirectoryDuplicateRemoval(DirName)

    end_time = time.time()

    total_time = end_time-start_time

    print("Total execution time required : ", (total_time))

if __name__ == "__main__":
    main()