# 2: Design a Python application that creates two threads.

# Thread 1 should calculate and display the maximum element from an list.
# Thread 2 should calculate and display the minimum element from the same list.
# The list should be accepted from the user.

import threading

def Maximum(List):
    Max = 0
    Max = List[0]

    for i in List:
        if Max < i:
            Max = i
    print("Max from List is : ",Max)

def Minimum(List):
    Min = 0
    Min = List[0]

    for i in List:
        if Min > i:
            Min = i
    print("Min from List is : ",Min)

def main():
    print("Start of main()")

    No = int(input("Enter size of list : "))

    List = list()

    for i in range(No):
        Num = int(input(f"Enter {i+1} element : "))
        List.append(Num)

    Max = threading.Thread(target=Maximum, args=(List, ))
    Min = threading.Thread(target=Minimum, args=(List, ))

    Max.start()
    Min.start()

    Max.join()
    Min.join()

    print("End of main()")

if __name__ == "__main__":
    main()