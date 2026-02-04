# 3. Write a program which contains filter(), map() and reduce() in it. 
# Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which greater than or equal to 70 and 
# less than or equal to 90. Map function will increase each number by 10. 
# Reduce will return product of all that numbers.

from functools import reduce

Function = lambda List : list(filter(lambda No : No if No > 70 and No <= 90 else None, List))

Increase = lambda List : list(map(lambda No : No+10, List))

Product = lambda List : reduce(lambda x,y : x*y, List)

def main():
    No = int(input("Enter size of list : "))

    List = list()
    FillList = 0
    Ret = 0

    for i in range(No):
        FillList = int(input(f"Enter {i+1} element for list : "))
        List.append(FillList)

    Data1 = Function(List)
    print(Data1)

    Data2 = Increase(Data1)
    print(Data2)

    Ret = Product(Data1)
    print(Ret)

if __name__ == "__main__":
    main()