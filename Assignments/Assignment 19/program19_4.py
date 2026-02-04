# 4. Write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which are even. 
# Map function will calculate its square. 
# Reduce will return addition of all that numbers.

from functools import reduce

def Function(List):
    Data = list(filter(lambda No : No if No %2 == 0 else None, List))
    print(Data)

    List2 = list(map(lambda No : No**2, Data))
    print(List2)

    Ret = reduce(lambda x,y : x+y, Data)
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