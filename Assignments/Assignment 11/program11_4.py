# 4. Write a program which accepts one number and prints reverse of that number.

# Input: 121

# Output: 321

def PrintReverse(No):
    iDigit = 0
    iReverse = 0

    while(No != 0):
        iDigit = No % 10
        iReverse = iReverse*10 + iDigit
        No = No // 10

    return iReverse

def main():
    Ret = 0
    Ret = PrintReverse(123)
    print(Ret)

if __name__ == "__main__":
    main()