# 5. Write a program which accept one number for user and check whether number is 
# prime or not.

def Prime(No):
    Flag = False

    for i in range(2,No+1//2):
        if No%i == 0:
            Flag = True 
            break

    return Flag

def main():
    No = int(input("Enter number : "))
    Ret = Prime(No)

    if(Ret == False):
        print("Is Prime")
    else:
        print("Is not Prime")

if __name__ == "__main__":
    main()