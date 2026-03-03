# 2. Design automation script which accept directory name and two file extensions from user.
# Rename all files with first file extension with the second file extenntion.

# Usage : DirectoryRename.py “Demo” “.txt” “.doc”

# Demo is name of directory and .txt is the extension that we want to search and rename
# with .doc.

# After execution this script each .txt file gets renamed as .doc.

import sys
import DirectoryRename

def main():
    DirName = sys.argv[1]
    Extension1 = sys.argv[2]
    Extension2 = sys.argv[3]
    
    DirectoryRename.DirectoryRename(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()