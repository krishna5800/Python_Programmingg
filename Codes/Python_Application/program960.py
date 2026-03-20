def main():
    size = 0
    Value = 0

    Arr = []  

    print("Enter the number of element : ")
    size = int(input())

    print("Enter the elements : ")

    for i in range(size):
        Value = int(input())
        Arr.append(Value)

    print(Arr)

main()