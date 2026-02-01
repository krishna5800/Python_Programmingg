import sys
import os

def DirectoryScanner(DirName = "Marvellous"):
    Ret = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("Their is no such directory")
        return
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for FName in FileName:
            print("File Name : ",FName)
            print("File Size : ", os.path.getsize(os.path.abspath(FName)))      # Path Issue

def main():
    Border = "-"*49
    print(Border)
    print("-------- Marvellous Directory Automation --------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid Number of arguments")
        print("Please specify the name of directory")
        return
    
    DirectoryScanner(sys.argv[1])
    
    print(Border)

if __name__== "__main__":
    main()