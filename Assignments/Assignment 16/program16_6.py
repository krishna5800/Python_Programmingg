# 6. Write a program which accept number from user and check 
# whether that number is positive or negative or zero.

def Check(No):
    if(No > 0):
        print("Positive")
    elif(No < 0):
        print("Negative")
    else:
        print("No is zero")

def main():
    Check(54)

if __name__ == "__main__":
    main()