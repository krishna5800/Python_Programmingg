# 1. Write a program which accept N numbers from user and store it into List.
#  Return addition of all elements from that List.

def AddList(List):
    Sum = 0

    for i in range(len(List)):
        Sum = Sum + List[i]

    return Sum

def main():
    No = int(input("Enter size of list : "))
    List = list()
    FillList = 0
    Ret = 0

    for i in range(No):
        FillList = int(input(f"Enter {i+1} element for list : "))
        List.append(FillList)

    Ret = AddList(List)
    print("Addition is : ", Ret)

if __name__ == "__main__":
    main()