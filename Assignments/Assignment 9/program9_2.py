# 2. Write a program which contains one function ChkGreater() that accepts 
# two numbers and prints the greater number.

# Input: 10 20

# Output: 20 is greater

def ChkGreater(No1 , No2):
    if (No1 > No2):
        return No1
    else:
        return No2

def main():
    Ret = 0
    Ret = ChkGreater(11,10)
    print(Ret)

if __name__ == "__main__":
    main()