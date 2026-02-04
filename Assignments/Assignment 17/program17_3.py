# 3. Write a program which accept one number from user and return its factorial Input:

def Factorial(No):
    iFact = 1

    for i in range(1,No+1):
        iFact = iFact * i

    return iFact

def main():
    No = int(input("Enter number : "))
    Ret = 0

    Ret = Factorial(No)
    print(Ret)

if __name__ == "__main__":
    main()