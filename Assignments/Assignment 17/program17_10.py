# 10. Write a program which accept number from user and return addition of digits in that number

# Input: 5187934

# Output: 37

def DisplayCount(No):
    Count = 0
    Digit = 0

    while(No != 0):
        Digit = No % 10
        Count = Count + Digit
        No = No//10

    return Count

def main():
    No = int(input("Enter number : "))

    Ret = DisplayCount(No)

    print(Ret)
    
if __name__ == "__main__":
    main()