# 2. Write a program which contains one lambda function which accepts two parameters 
# and return its multiplication.

Mul = lambda No1, No2 : No1*No2

def main():
    No1 = int(input("Enter first number :"))
    No2 = int(input("Enter second number :"))

    Ret = Mul(No1, No2)

    print(Ret)

if __name__ == "__main__":
    main()