import os

def DirectoryFileSearch(DirName, Extension):

    FileList = []
    ReturnList = []

    if(os.path.exists(DirName) == True and os.path.isdir(DirName) == True):

        for FolderName, SubFolderName, FileName in os.walk(DirName):

            FileList.extend(FileName)
            break

        for f in FileList:
            list = f.split(".")

            if list[1] == Extension:
                ReturnList.append(f)

            list = []

    return ReturnList