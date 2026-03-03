# 3. Design automation script which accept two directory names. 
# Copy all files from first directoryvinto second directory. 
# Second directory should be created at run time.

# Usage : DirectoryCopy.py “Demo” “Temp”
# Demo is name of directory which is existing and contains files

import sys
import DirectoryCopy

def main():
    DirSrc = sys.argv[1]
    DirDest = sys.argv[2]

    DirectoryCopy.DirectoryCopy(DirSrc, DirDest)

if __name__ == "__main__":
    main()