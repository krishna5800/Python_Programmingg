# 1.Create on module named as Arithmetic which contains 4 functions as Add() 
# for addition, Sub() for subtraction, Mult() for multiplication and Div() for division. 
# All functions accepts two parameters as number and perform the operation. Write on python 
# program which call all the functions 
# from Arithmetic module by accepting the parameters from user.

import Arithematic as a

def main():
    No1 = int(input("Enter first Number : "))
    No2 = int(input("Enter second Number : "))

    Ret = a.Add(No1,No2)
    print("Addition is : ", Ret)

    Ret = a.Sub(No1,No2)
    print("Substraction is : ", Ret)

    Ret = a.Mul(No1,No2)
    print("Multiplication is : ", Ret)

    Ret = a.Div(No1,No2)
    print("Division is : ", Ret)

if __name__ == "__main__":
    main()