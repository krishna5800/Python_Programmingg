class Arithmatic:
    # Coustuctor

    def __init__(self,A = 0,B = 0):  # Default Argument
        self.No1 = A        # characterstics
        self.No2 = B        # characterstics

    def Addition(self):
        Ans = 0
        Ans = self.No1 + self.No2
        return Ans

    def Substraction(self):
        Ans = 0
        Ans = self.No1 - self.No2
        return Ans
    
def main():

    aboj = Arithmatic()

    Ret = aboj.Addition()

    print("The Addition is : ",Ret )

    Ret = aboj.Substraction()

    print("The Substraction is : ",Ret )

main()