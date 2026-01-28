# 4. Write a program which accepts one number and prints cube of that number.

# Input: 5 
# Output: 125

def CubeNum(No):
    return No**3

def main():
    Ret = 0
    Ret = CubeNum(5)
    print(Ret)

if __name__ == "__main__":
    main()