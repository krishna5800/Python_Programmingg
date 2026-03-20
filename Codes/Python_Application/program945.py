def CheckOddEven(No):
    if No % 2 == 0:
        print("It is Even number")
    else:
        print("It is Odd number")


def main():
    print("Enter number : ")
    Value = int(input())

    CheckOddEven(Value)
        
main()