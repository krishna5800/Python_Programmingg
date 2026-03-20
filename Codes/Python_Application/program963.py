def Minimum(Brr):

    iMin = Brr[0]

    for i in range(len(Brr)):
        if Brr[i] < iMin:
            iMin = Brr[i]
        
    return iMin

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

    Ret = Minimum(Arr)

    print("Minimum number is : ",Ret)

main()