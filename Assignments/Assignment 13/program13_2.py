# 2. Write a program which accepts radius of circle and prints area of circle.

def AreaCircle(Radius, Pi = 3.14):
    return (Radius*Radius*Pi)

def main():
    Ret = 0
    Ret = AreaCircle(10)
    print("Area is :", Ret)

if __name__ == "__main__":
    main()