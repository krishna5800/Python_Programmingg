# 3. Write a program which accepts one number and prints square of that number.

# Input: 5 
# Output: 25

def SquareNum(No):
    return No**2

def main():
    Ret = 0
    Ret = SquareNum(5)
    print(Ret)

if __name__ == "__main__":
    main()