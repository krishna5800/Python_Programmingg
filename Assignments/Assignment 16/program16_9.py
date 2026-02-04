# 9. Write a program which display first 10 even numbers on screen

def FirstTenEven():
    Count = 0
    i = 1

    while(Count < 10):
        if(i % 2 == 0):
            print(i)
            Count = Count + 1
        i = i + 1

def main():
    FirstTenEven()

if __name__ == "__main__":
    main()