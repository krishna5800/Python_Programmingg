def CountCaptial(Brr):
    iCount = 0

    for ch in Brr:
        if ((ch >= 65 and ch <= 90)):               # issue
            iCount = iCount+1

    return iCount

def main():
    print("Enter a string : ")
    Arr = input()

    Ret = CountCaptial(Arr)

    print("Number of captial charecters are : ",Ret)
        
main()