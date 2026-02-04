# 2. Write a program which accept N numbers from user and store it into List. 
# Return Maximum number from that List.

def Maximum(List):
    Max = 0

    Max = List[0]

    for i in range(len(List)):
        if Max < List[i]:
            Max =List[i]

    return Max

def main():
    No = int(input("Enter size of list : "))
    List = list()
    FillList = 0
    Ret = 0

    for i in range(No):
        FillList = int(input(f"Enter {i+1} element for list : "))
        List.append(FillList)

    Ret = Maximum(List)
    print("Maximum is : ", Ret)

if __name__ == "__main__":
    main()