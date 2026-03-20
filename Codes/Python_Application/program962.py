def Maximum(Brr):

    iMax = Brr[0]

    for i in range(len(Brr)):
        if Brr[i] > iMax:
            iMax = Brr[i]
        
    return iMax


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

    Ret = Maximum(Arr)

    print("Maximum number is : ",Ret)

main()