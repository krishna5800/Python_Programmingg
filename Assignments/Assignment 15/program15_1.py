# 1. Write a lambda function using map() which accepts a list of 
# numbers and returns a list of squares of each number.

Square = lambda nums : list(map(lambda No : No**2, nums))

def main():
    nums = [1,2,3,4,5]

    Data = Square(nums)

    print(Data)

if __name__ == "__main__":
    main()