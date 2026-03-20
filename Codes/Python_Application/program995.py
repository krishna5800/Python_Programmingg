class ArrayX:
    def __init__(self, size):
        self.size = size
        self.Arr = [0] * size

    def Accept(self):
        print("Enter elements : ")

        for i in range(0, self.size):
            Value = int(input())
            self.Arr[i] = Value
    
    def Display(self):
        print("Elements of the array are : ")

        for i in range(0, self.size):
            print(self.Arr[i])

    def Summation(self):
        Sum = 0
        
        for i in range(0, self.size):
            Sum = Sum + self.Arr[i]

        return Sum

def main():

    aobj  = ArrayX(5)

    aobj.Accept()
    aobj.Display()
    print("Summation is : ", aobj.Summation())

if __name__ == "__main__":
    main()