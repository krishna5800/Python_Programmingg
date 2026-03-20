def CountCaptial(Brr):
    iCount = 0

    for i in range(len(Brr)):
        if ((Brr[i] >= "A" and Brr[i] <= "Z")):
            iCount = iCount+1

    return iCount

def main():
    print("Enter a string : ")
    Arr = input()

    Ret = CountCaptial(Arr)

    print("Number of captial charecters are : ",Ret)
        
main()