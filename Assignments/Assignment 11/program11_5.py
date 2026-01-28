# 5. Write a program which accepts one number and checks whether it is palindrome or not.

# Ingrat: 121 
# Outputs : Palindrome

def ChkPalindrome(No):
    iReverse = 0
    iDigit = 0 
    iValue = No
    Flag = False

    while No != 0:
        iDigit = No % 10
        iReverse = iReverse*10 + iDigit
        No = No // 10

    if(iReverse == iValue):
        Flag = True

    return Flag


def main():
    Ret = False

    Ret = ChkPalindrome(121)

    if(Ret == True):
        print("Is Palindrome")
    else:
        print("Not Palindrome")


if __name__ == "__main__":
    main()