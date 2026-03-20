def CountCaptial(Brr):
    iCount = 0

    for i in range(len(Brr)):
        if ((Brr[i] >= 65 and Brr[i] <= 90)):               # issue
            iCount = iCount+1

    return iCount

def main():
    print("Enter a string : ")
    Arr = input()

    Ret = CountCaptial(Arr)

    print("Number of captial charecters are : ",Ret)
        
main()