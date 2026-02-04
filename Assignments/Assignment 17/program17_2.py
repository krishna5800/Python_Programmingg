# 2. Write a program which accept one number and display below pattern. 

# Input: 5

# Output:     *   *   *   *   *
#             *   *   *   *   *
#             *   *   *   *   *
#             *   *   *   *   *
#             *   *   *   *   *

def Display(No):
    for i in range(No):
        for j in range(No):
            print("*", end = " ")

        print()


def main():
    No = int(input("Enter number : "))
    Display(No)

if __name__ == "__main__":
    main()