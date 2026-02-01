import sys
import os

def DirectoryScanner(DirName = "Marvellous"):
    Border = "-"*55

    fobj = open("Marvellous.log", "w")

    fobj.write(Border + "\n")
    fobj.write("This is a log file created by Marvellous Automation" + "\n")
    fobj.write("This is a Directory Cleaner Script" + "\n")
    fobj.write(Border + "\n")

    Ret = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("Their is no such directory")
        return
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    FileCount = 0
    EmptyFileCount = 0
    
    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for FName in FileName:
            FileCount = FileCount + 1

            FName = os.path.join(FolderName, FName)

            if(os.path.getsize(os.path.abspath(FName)) == 0):       # Empty File
                EmptyFileCount = EmptyFileCount + 1
                os.remove(FName)

    fobj.write("Total files scanned : " + str(FileCount) + "\n")
    fobj.write("Total empty files found : " + str(EmptyFileCount) + "\n")
    fobj.write(Border + "\n")

    fobj.close()

def main():
    Border = "-"*55
    print(Border)
    print("----------- Marvellous Directory Automation -----------")
    print(Border)

    if(len(sys.argv) != 2):
        print("Invalid Number of arguments")
        print("Please specify the name of directory")
        return
    
    DirectoryScanner(sys.argv[1])
    
    print(Border)
    print("----------- Thank You For Using Application -----------")
    print(Border)

if __name__== "__main__":
    main()