# 2: Design a Python application that creates two threads named EvenFactor and OddFactor.

# Both threads should accept one integer number as a parameter.

# The EvenFactor thread should:
# Identify all even factors of the given number.
# Calculate and display the sum of even factors

# The OddFactor thread should:
# Identify all odd factors of the given number
# Calculate and display the sum of odd factors.

# After both threads complete execution, the main thread should display the message.
# "Exit from main"

import threading

def EvenFactors(No):
    Sum = 0

    for i in range(1,No+1//2):
        if No % i == 0:
            if i % 2 == 0:
                Sum = Sum + i

    print("Sum of Even factors : ", Sum)

def OddFactors(No):
    Sum = 0

    for i in range(1,No+1//2):
        if No % i == 0:
            if i % 2 != 0:
                Sum = Sum + i

    print("Sum of Odd factors : ", Sum)

def main():

    print("Start of main()")
    
    Evenfactor = threading.Thread(target=EvenFactors, args=(12,))
    OddFactor = threading.Thread(target=OddFactors, args=(12,))

    Evenfactor.start()
    OddFactor.start()

    Evenfactor.join()
    OddFactor.join()

    print("End of main()")

if __name__ == "__main__":
    main()