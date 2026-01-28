# 4. Write a program which accepts one number and prints binary equivalent.

def BinaryEquivalent(No):
    Digit = 0
    Ans = ""

    while(No != 0):
        Digit = No % 2
        No = No // 2
        Ans += str(Digit)

    return Ans[::-1]

def main():
    Ret = ""
    Ret = BinaryEquivalent(10)

    print(Ret)

if __name__ == "__main__":
    main()