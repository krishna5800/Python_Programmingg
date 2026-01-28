# 2. Write a program which accepts one number and prints its factors.

# Input: 12

# Output: 1 2 3 4 6 12

def FindFactors(Value):
    for i in range(1,(Value//2 + 10)):
        if(Value%i == 0):
            print(i)

def main():
    FindFactors(12)

if __name__ == "__main__":
    main()