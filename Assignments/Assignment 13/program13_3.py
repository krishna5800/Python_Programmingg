# 3. Write a program which accepts one number and checks whether it is perfect number or not.

# Input: 6

# Output: Perfect Number

def PerfectNumber(No):
    Sum = 0
    Flag = False

    for i in range(1,(No//2+1)):
        if(No % i) == 0:
            Sum = Sum + i

    if(Sum == No):
        Flag = True

    return Flag

def main():
    Ret = False

    Ret = PerfectNumber(6)

    if(Ret == True):
        print("Perfect Number")
    else:
        print("Not Perfect Number")

if __name__ == "__main__":
    main()