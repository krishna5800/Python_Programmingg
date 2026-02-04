# 1. Write a program which contains one lambda function 
# which accepts one parameter and return power of two

Power = lambda No : No**2

def main():
    No = int(input("Enter number :"))

    Ret = Power(No)

    print(Ret)

if __name__ == "__main__":
    main()