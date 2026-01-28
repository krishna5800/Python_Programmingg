# 5.Write a program which accepts one number and prints all odd numbers till that number.

def PrintOdd(No):

    for i in range(1,No+1,2):
        print(i)

def main():
    PrintOdd(10)

if __name__ == "__main__":
    main()