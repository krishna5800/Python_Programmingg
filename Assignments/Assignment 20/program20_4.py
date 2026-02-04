# 4: Design a Python application that creates three threads named Small, Capital, and Digits.

# All threads should accept a string as input.

# The Small thread should count and display the number of lowercase characters.

# The Capital thread should count and display the number of uppercase characters.

# The Digits thread should count and display the number of numeric digits.

# Each thread must also display:
# Thread ID
# Thread Name

import threading

def CountSamll(String):
    print("Current Thread ID : ", threading.get_ident())
    print("Current Thread Name : ", threading.current_thread().name)
    Tup = tuple(String)
    Count = 0

    for i in Tup:
        if i.islower() == True:
            Count = Count + 1

    print("Count of lowercase characters : ", Count)

def CountCapital(String):
    print("Current Thread ID : ", threading.get_ident())
    print("Current Thread Name : ", threading.current_thread().name)
    Tup = tuple(String)
    Count = 0

    for i in Tup:
        if i.isupper() == True:
            Count = Count + 1

    print("Count of uppercase characters : ", Count)

def CountDigits(String):
    print("Current Thread ID : ", threading.get_ident())
    print("Current Thread Name : ", threading.current_thread().name)
    Tup = tuple(String)
    Count = 0

    for i in Tup:
        if i.isdigit() == True:
            Count = Count + 1

    print("Count of digits : ", Count)

def main():
    print("Start of main()")

    Str = input("Enter String : ")

    Small  = threading.Thread(target=CountSamll, args=(Str,))

    Capital = threading.Thread(target=CountCapital, args=(Str,))

    Digits = threading.Thread(target=CountDigits, args=(Str,))

    Small.start()
    Capital.start()
    Digits.start()

    Small.join()
    Capital.join()
    Digits.join()

    print("End of main()")

if __name__ == "__main__":
    main()