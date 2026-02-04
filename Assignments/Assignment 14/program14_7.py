# 7. Write a lambda function which accepts one number and returns True if divisible by 5.

DivByFive = lambda No : True if No%5 == 0 else False

def main():
    Ret = (DivByFive(11))

    if(Ret == True):
        print("Is Odd")
    else:
        print("Is not Odd")

if __name__ == "__main__":
    main()