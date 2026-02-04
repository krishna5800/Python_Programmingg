# 9. Write a program which accept number from user and return number of digits in that number.

# Input: 5187934

# Output: 7

def DisplayCount(No):
    Count = 0

    while(No != 0):
        Count = Count + 1
        No = No//10

    return Count

def main():
    No = int(input("Enter number : "))

    Ret = DisplayCount(No)

    print(Ret)
    
if __name__ == "__main__":
    main()