# 5. Write a program which accepts one number and checks whether it is divisible by 3 and 5

# Input: 15

# Output: Divisible by 3 and 5

def ChkDivBy3and5(No):
    FLag = False

    if(No%3 == 0 and No%5 == 0):
        FLag = True
    
    return FLag


def main():
    Ret = False

    Ret = ChkDivBy3and5(15)

    if(Ret):
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")

if __name__ == "__main__":
    main()