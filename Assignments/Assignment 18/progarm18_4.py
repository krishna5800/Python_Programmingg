# 4. Write a program which accept N numbers from user and store it into List. 
# Accept one another inte a program which accept number from user and return
# frequency of that number from List.

def Frequency(List, Target):
    Freq = 0

    for i in range(len(List)):
        if(List[i] == Target):
            Freq = Freq + 1

    return Freq

def main():
    No = int(input("Enter size of list : "))
    Freq = int(input("Enter target element : "))

    List = list()
    FillList = 0
    Ret = 0

    for i in range(No):
        FillList = int(input(f"Enter {i+1} element for list : "))
        List.append(FillList)

    Ret = Frequency(List, Freq)
    print("Frequency is : ", Ret)

if __name__ == "__main__":
    main()