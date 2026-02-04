# 7. Write a program which contains one function that accept one number from user and returns 
# true if number is divisible by 5 otherwise return false.

def DivisibleByFive(No):
    return (No%5 == 0)

def main():
    Ret = DivisibleByFive(8)

    if(Ret == True):
        print("Divisible by 5")
    else:
        print("Not divisible by 5")

if __name__ == "__main__":
    main()