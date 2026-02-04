# 10. Write a lambda function using filter() which accepts a 
# list of numbers and returns the count of even numbers

Product = lambda nums : len(list(filter(lambda No : No%2 == 0, nums)))

def main():
    nums = [1,2,3,4,5,6]

    Data = Product(nums)

    print(Data)

if __name__ == "__main__":
    main()