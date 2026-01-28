# 1. Write a program which accepts one number and checks whether it is prime or not.

# Input: 11

# Output: Prime Number

def ChkPrime(No):
    Flag = False

    for i in range(2,No,1):
        if(No % i == 0):
            Flag = True

    return Flag

def main():
    Ret = False

    Ret = ChkPrime(11)

    if(Ret == True):
        print("Not Prime")
    else:
        print("Is Prime")

if __name__ == "__main__":
    main()