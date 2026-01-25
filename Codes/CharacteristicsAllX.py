class Demo:
    No = 10

    def __init__(self, A, B):
        self.Value1 = A
        self.Value2 = B

print("Class variable : ",Demo.No)

obj1 = Demo(11,21)
obj2 = Demo(51,101)

# print(obj1.No)                            ALLOWED BUT NOT GOOD PROGRAMMING PRACTISE

print("Instance Variable of obj1 : ", obj1.Value1, obj1.Value2)     # 11    21
print("Instance Variable of obj2 : ", obj2.Value1, obj2.Value2)     # 51    101

obj1.Value1 = 15

# Demo.No = 0
obj1.No = 0

print("Instance Variable of obj1 : ", obj1.Value1, obj1.Value2)     # 15    21
print("Instance Variable of obj2 : ", obj2.Value1, obj2.Value2)     # 51    101

print(obj1.No)      # 0
print(obj2.No)      # 0 expected but is 10 


# From python 2.6 onwards the when Class vairable is accessed for changing value then it will 
# create an copy for the object and it will not change the copy and not the original class variable