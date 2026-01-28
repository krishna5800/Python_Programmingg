# 3. Write a program which accepts one number and prints sum of digits.

# Input: 123

# Output: 6

def SumDigit(No):
    iDigit = 0
    iSum = 0

    while(No != 0):
        iDigit = No % 10
        iSum = iSum + iDigit
        No = No // 10

    return iSum

def main():
    Ret = 0

    Ret = SumDigit(123)
    print(Ret)

if __name__ == "__main__":
    main()