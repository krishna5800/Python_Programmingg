# 10. Write a lambda function which accepts three numbers and returns largest number.

LargestOfThree = lambda No1, No2, No3 : No1 if No1>No2 and No1>No3 else No2 if No2>No1 and No2>No3 else No3

def main():
    print(LargestOfThree(1,2,3))

if __name__ == "__main__":
    main()