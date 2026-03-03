# 4. Design automation script which accept two directory names and one file extension. 
# Copy all files with the specified extension from first directory into second directory. 
# Second directory should be created at run time.

# Usage : DirectoryCopyExt.py “Demo” “Temp” “.exe”
# Demo is name of directory which is existing and contains files in it. 
# We have to create new Directory as Temp and copy all files with extension .exe from 
# Demo to Temp.

import sys
import DirectoryCopyExt

def main():
    DirSrc = sys.argv[1]
    DirDest = sys.argv[2]
    Extension = sys.argv[3]

    DirectoryCopyExt.DirectoryCopyExt(DirSrc, DirDest, Extension)

if __name__ == "__main__":
    main()