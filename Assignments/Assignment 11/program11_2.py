# 2.Write a program which accepts one number and prints count of digits in that number.

# Input : 7521

# Output : 4

def CountDigit(No):
    iCount = 0

    while(No != 0):
        iCount = iCount + 1
        No = No // 10

    return iCount

def main():
    Ret = 0

    Ret = CountDigit(1111)
    print(Ret)

if __name__ == "__main__":
    main()