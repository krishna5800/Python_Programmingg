# 5. Write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all prime numbers. 
# Map function will multiply each number by 2. 
# Reduce will retum Maximum number from that numbers. 
# (You can also use normal functions instead of lambda functions).

from functools import reduce

def IsPrime(No):
    Flag = False

    for i in range(2,No+1//2,1):
        if No % i == 0:
            Flag = True
            break

    if Flag == False:
        return No
    else:
        return None

def Function(List):

    Data = list(filter(IsPrime, List))
    print(Data)

    List2 = list(map(lambda No : No * 2, Data))
    print(List2)

    Ret = reduce(lambda x,y : x if x > y else y, List)
    print(Ret)

def main():
    No = int(input("Enter size of list : "))

    List = list()

    for i in range(No):
        FillList = int(input(f"Enter {i+1} element for list : "))
        List.append(FillList)

    Function(List)

if __name__ == "__main__":
    main()