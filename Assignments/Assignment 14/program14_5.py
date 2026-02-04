# 5. Write a lambda function which accepts one number and returns True 
# if number is even otherwise False.

Even = lambda No : True if No%2 == 0 else False

def main():
    Ret = (Even(11))

    if(Ret == True):
        print("Is Even")
    else:
        print("Is not Even")

if __name__ == "__main__":
    main()