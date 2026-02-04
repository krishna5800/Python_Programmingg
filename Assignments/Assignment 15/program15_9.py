# 9. Write a lambda function using reduce() which accepts a list of 
# numbers and returns the product of all elements.

from functools import reduce

Product = lambda nums : reduce(lambda x,y : x*y, nums)

def main():
    nums = [1,2,3,4,5]

    Data = Product(nums)

    print(Data)

if __name__ == "__main__":
    main()