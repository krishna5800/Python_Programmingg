# 3: Design a Python application where multiple threads update a shared variable.

# Use a Lock to avoid race conditions.
# Each thread should increment the shared counter multiple times.
# Display the final value of the counter after all threads complete execution

import threading

No = 0
lobj = threading.Lock()

def Increment():
    global No

    for _ in range(200000):
        with lobj:
            No = No+1

def main():
    print("Start of main()")

    global No

    Thread1 = threading.Thread(target=Increment)
    Thread2 = threading.Thread(target=Increment)

    Thread1.start()
    Thread2.start()

    Thread1.join()
    Thread2.join()

    print("Value of No is : ", No)

    print("End of main()")

if __name__ == "__main__":
    main()