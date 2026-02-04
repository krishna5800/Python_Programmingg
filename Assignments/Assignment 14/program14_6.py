# 6. Write a lambda function which accepts one number and returns True 
# if number is  odd otherwise False.

Odd = lambda No : False if No%2 == 0 else True

def main():
    Ret = (Odd(11))

    if(Ret == True):
        print("Is Odd")
    else:
        print("Is not Odd")

if __name__ == "__main__":
    main()