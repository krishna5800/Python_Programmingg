# 2. Write a lambda function using filter() which 
# accepts a list of numbers and returns a list of even numbers.

Even = lambda nums : list(filter(lambda No : No%2==0, nums))

def main():
    nums = [1,2,3,4,5]

    Data = Even(nums)

    print(Data)

if __name__ == "__main__":
    main()