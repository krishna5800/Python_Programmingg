# 2. Write a program which accepts one number and prints sum of first N natural numbers.

# Input: 5 
# Output: 15

def SunNatural(No):
    Sum = 0

    for i in range(1,(No+1),1):
        Sum = Sum + i

    return Sum

def main():
    Ret = 0
    Ret = SunNatural(5)
    print(Ret)

if __name__ == "__main__":
    main()