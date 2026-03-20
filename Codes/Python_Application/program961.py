def Summation(Brr):

    iSum = 0

    for no in Brr:
        iSum = iSum + no

    return iSum


def main():
    size = 0
    Value = 0

    Arr = []  

    print("Enter the number of element : ")
    size = int(input())

    print("Enter the elements : ")

    for i in range(size):
        Value = int(input())
        Arr.append(Value)

    Ret = Summation(Arr)

    print("Summation is : ",Ret)

main()