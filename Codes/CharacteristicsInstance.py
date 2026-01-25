import gc

class Demo:
    # Class Variable
    No1 = 10
    No2 = 11

    def __init__(self):
        # Instance Variable
        self.A = 101
        self.B = 201
        print("Inside Constructor")

    def __del__(self):
        print("Inside Destructor")

# Call for class variables don't need object
print(Demo.No1)
print(Demo.No2)

# Call for instance variable need object
obj = Demo()

print(obj.A)
print(obj.B)

del obj

gc.collect()