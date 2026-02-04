# 1: Design a Python application that creates two separate threads named Even and Odd.

# The Even thread should display the first 10 even numbers.
# The Odd thread should display the first 10 odd numbers.
# Both threads should execute independently using the threading module.
# Ensure proper thread creation and execution.

import threading

def EvenFirstTen():
    Count = 0
    i = 2
    print("Even :")

    while(Count < 10):
        print(i, end= "  ")
        i = i + 2
        Count = Count + 1

def OddFirstTen():
    Count = 0
    i = 1
    print("Odd :")

    while(Count < 10):
        print(i, end= "  ")
        i = i + 2
        Count = Count + 1

def main():

    t1 = threading.Thread(target= EvenFirstTen)
    t2 = threading.Thread(target=OddFirstTen)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()