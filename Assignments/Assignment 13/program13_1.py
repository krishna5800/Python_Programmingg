# 1. Write a program which accepts length and width of rectangle and prints area.

def AreaRect(Length, Width):
    return (Length*Width)

def main():
    Ret = 0
    Ret = AreaRect(10,10)
    print("Area is :", Ret)

if __name__ == "__main__":
    main()