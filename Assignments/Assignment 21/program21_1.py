# 1: Design a Python application that creates two threads named Prime and NonPrime.

# Both threads should accept a list of integers.
# The Prime thread should display all prime numbers from the list.
# The Non Prime thread should display all non-prime numbers from the list.

import threading

def PrimeFun(List):
    print("Prime numbers for list : ")
    Flag = False

    for i in List:
        Flag = False
        for j in range(2,i):
            if i % j == 0:
                Flag = True
                break

        if Flag == False:
            print(i)

def NonPrimeFun(List):
    print("Non-Prime numbers for list : ")
    Flag = False

    for i in List:
        Flag = False
        for j in range(2,i):
            if i % j == 0:
                Flag = True
                break

        if Flag == True:
            print(i)


def main():
    print("Start of main()")

    No = int(input("Enter size of list : "))

    List = list()

    for i in range(No):
        Num = int(input(f"Enter {i+1} element : "))
        List.append(Num)
    
    Prime = threading.Thread(target=PrimeFun, args=(List,))
    NonPrime = threading.Thread(target=NonPrimeFun, args=(List,))

    Prime.start()
    Prime.join()

    print()

    NonPrime.start()
    NonPrime.join()

    print("End of main()")

if __name__ == "__main__":
    main()