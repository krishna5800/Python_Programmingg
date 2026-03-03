# 1.Design automation script which accept directory name and display checksum of all files.
# Usage : DirectoryChecksum.py “Demo”
# Demo is name of directory.

import sys
import DirectoryChecksum

def main():
    DirName = sys.argv[1]

    DirectoryChecksum.DirectoryChecksum(DirName)

if __name__ == "__main__":
    main()