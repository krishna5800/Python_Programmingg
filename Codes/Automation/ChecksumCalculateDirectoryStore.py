import hashlib
import os

def CalculateChecksum(FileName):
    fobj = open(FileName, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirectoryName = "Marvellous"):
    Ret = False

    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("Their is no such directory")
        return
    
    Ret = os.path.isdir(DirectoryName)

    if(Ret == False):
        print("It is not a driectory")
        return
    
    Duplicate = {}
    
    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        
        for FName in FileName:
            FName = os.path.join(FolderName, FName)
            Checksum = CalculateChecksum(FName)

            if Checksum in Duplicate:
                Duplicate[Checksum].append(FName)
            else:
                Duplicate[Checksum] = [FName]

    return Duplicate

def DisplayResult(MyDixt):

    Result = list(filter(lambda x : len(x) > 1, MyDixt.values()))

    Count = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            print(subvalue)
        print("Value of count is : ", Count)
        Count = 0

def DeleteDuplicate(Path = "Marvellous"):
    MyDict = FindDuplicate(Path)

    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    Count = 0
    Cnt  = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if(Count > 1):
                print("Deleted File : ", subvalue)
                os.remove(subvalue)
                Cnt = Cnt + 1
        Count = 0

    print("Total Deleted Files : ", Cnt)

def main():
    Ret = FindDuplicate()

    DisplayResult(Ret)

    DeleteDuplicate()

if __name__ == "__main__":
    main()