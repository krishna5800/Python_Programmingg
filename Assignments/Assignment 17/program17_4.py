# 4. Write a program which accept one number form user and return addition of its factors.

def Factors(No):
    Sum = 0

    for i in range(1,No+1//2):
        if No % i == 0:
            Sum = Sum + i

    return Sum

def main():
    No = int(input("Enter number :"))

    Ret = Factors(No)

    print(Ret)

if __name__ == "__main__":
    main()