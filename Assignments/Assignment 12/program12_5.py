# 5. Write a program which accepts one number and prints that many numbers in reverse order.

# Input: 5

# Output: 54321

def PrintNumbersReverse(No):
    for i in range(5,0,-1):
        print(i)

def main():
    PrintNumbersReverse(5)

if __name__ == "__main__":
    main()