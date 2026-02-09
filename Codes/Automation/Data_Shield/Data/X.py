import os

def main():
    DirectoryName = input("Enter the name of directory : ")

    print("Contents of the directory : ")

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        print("FolderName : ", FolderName)

        for SubF in SubFolderName:
            print("SubFolderName : ", SubF)

        for FName in FileName:
            print("FileName : ", FName)

if __name__ == "__main__":
    main()