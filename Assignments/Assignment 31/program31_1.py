# 1.Design automation script which accept directory name and file extension from user. 
# Display all files with that extension.

# Usage : DirectoryFileSearch.py “Demo” “.txt”

# Demo is name of directory and .txt is the extension that we want to search.

import sys
import DirectoryFileSearch

def main():
    DirName = sys.argv[1]
    Extension = sys.argv[2]
    List = DirectoryFileSearch.DirectoryFileSearch(sys.argv[1], sys.argv[2])

    print(List)

if __name__ == "__main__":
    main()