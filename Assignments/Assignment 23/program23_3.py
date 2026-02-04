# 3: Write a Python program to implement a class named Numbers with the following specifications:

# The class should contain one instance variable: Value

# Define a constructor (init) that accepts a number from the user and initializes Value.

# Implement the following instance methods:
# ChkPrime()-returns True if the number is prime, otherwise returns False
# ChkPerfect()-returns True if the number is perfect, otherwise returns False
# Factors()-displays all factors of the number
# SumFactors()returns the sum of all factors (You may use this method as a helper in ChkPerfect() if required)

# Create multiple objects and call all methods.

class Numbers:

    def __init__(self, A):
        self.Value = A

    def ChkPrime(self):
        self.Flag = False

        for i in range(2,self.Value):
            if self.Value % i == 0:
                self.Flag = True
                break

        return self.Flag
    
    def ChkPerfect(self):
        self.Flag1 = False
        self.Sum = 0

        for i in range(2,self.Value):
            if self.Value % i == 0:
                self.Sum = self.Sum + i

        if self.Sum + 1 == self.Value:
            self.Flag1 = True

        return self.Flag1
    
    def Factors(self):
        print("Factors are : ")
        for i in range(2,self.Value):
            if self.Value % i == 0:
                print(i)

    def SumFactors(self):
        self.SumFactors = 0

        for i in range(2,self.Value):
            if self.Value % i == 0:
                self.SumFactors = self.SumFactors + i

        print("Sum of Factors is : ", self.SumFactors)

def main():
    obj = Numbers(6)
    Ret = False

    Ret = obj.ChkPrime()
    if Ret == True:
        print("Not Prime")
    else:
        print("Prime")

    Ret = obj.ChkPerfect()
    if Ret == True:
        print("Is Perfect")
    else:
        print("Not Perfect")

    obj.Factors()

    obj.SumFactors()

if __name__ == "__main__":
    main()