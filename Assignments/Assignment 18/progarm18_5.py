# 5. Write a program which accept N numbers from user and store it into List. 
# Return addition of all prime numbers from that List. 
# Main python file accepts N numbers from user and pass each number to ChikPrime() function 
# which is part of our user defined module named as MarvellousNum. 
# Name of the function from main python file should be ListPrime().

import MarvellousNum as m

def main():
    No = int(input("Enter size of list : "))

    List = list()
    FillList = 0
    Ret = 0

    for i in range(No):
        FillList = int(input(f"Enter {i+1} element for list : "))
        List.append(FillList)

    Ret = m.AddPrime(List)
    print("Addition of prime numbers in list is : ", Ret)

if __name__ == "__main__":
    main()