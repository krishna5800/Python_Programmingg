# 3.Write a program which accept N numbers from user and store it into List. 
# Return Minimum number from that List.

def Minimum(List):
    Minimum = 0

    Minimum = List[0]

    for i in range(len(List)):
        if Minimum > List[i]:
            Minimum =List[i]

    return Minimum

def main():
    No = int(input("Enter size of list : "))
    List = list()
    FillList = 0
    Ret = 0

    for i in range(No):
        FillList = int(input(f"Enter {i+1} element for list : "))
        List.append(FillList)

    Ret = Minimum(List)
    print("Minimum is : ", Ret)

if __name__ == "__main__":
    main()