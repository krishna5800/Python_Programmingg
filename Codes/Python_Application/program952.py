def SumDigits(No):
    Digit = 0
    iSum = 0

    while(No != 0):
        Digit =  No % 10
        iSum = iSum + Digit
        No = No // 10       # Floor division
    
    return iSum

def main():
    No = 0

    print("Enter a number : ")
    No = int(input())

    Ret = SumDigits(No)

    print("Summnation of Digits",Ret)
     
main()