import os
import schedule

def DirectoryScanner(DirectoryName = "Marvellous"):

    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("Their is no such directory")
        return
    
    Ret = os.path.isdir(DirectoryName)

    if(Ret == False):
        print("Unable to scan as it is not a directory")
        return

    print("Contents of the directory : ")

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
            print("FolderName : ", FolderName)

            for SubF in SubFolderName:
                print("SubFolderName : ", SubF)

            for FName in FileName:
                print("FileName : ", FName)

def main():
    DirectoryName = input("Enter the name of directory : ")

    DirectoryScanner(DirectoryName)
    
if __name__ == "__main__":
    main()