# 4: Design a Python application that creates two threads.

# Thrend 1 should compute the sum of elements from a list.
# Thread 2 should compute the product of elements from the same Int.

# Return the resurs to the main thread and display them.

import threading

def SumList(List, result):
    Sum = 0

    for i in List:
        Sum = Sum + i

    result['Sum'] = Sum

def ProductList(List, result):
    Mul = 1

    for i in List:
        Mul = Mul * i

    result['Product'] = Mul

def main():
    print("Start of main()")

    No = int(input("Enter size of list : "))

    List = list()

    for i in range(No):
        Num = int(input(f"Enter {i+1} element : "))
        List.append(Num)

    result = {}

    Thread1 = threading.Thread(target=SumList, args=(List,result,))
    Thread2 = threading.Thread(target=ProductList, args=(List,result,))

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

    print("Sum is : ", result.get('Sum'))
    print("Product is :", result.get('Product'))

    print("End of main()")

if __name__ == "__main__":
    main()