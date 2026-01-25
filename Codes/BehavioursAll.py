class Demo:
    No = 10

    def __init__(self,A,B):
        self.Value1 = A
        self.Value2 = B

    def fun(self):
        print("Inside instance method fun",self.Value1,self.Value2)
    
    @classmethod
    def sun(cls):                               # Class method comp
        print("Inside Class method sun",cls.No)
    
    @staticmethod           # no comp
    def gun():
        print("Inside Static Method",Demo.No)        # can access class variable

Demo.sun()

print("Class variable No : ",Demo.No)

obj = Demo(11,21)

obj.fun()
print("Instance Variable : ",obj.Value1,obj.Value2)

Demo.gun()