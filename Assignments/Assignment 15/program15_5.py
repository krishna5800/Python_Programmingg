# 5. Write a lambda function using reduce() which accepts 
# a list of numbers and returns the maximum element.

from functools import reduce

Max = lambda nums : (reduce(lambda x, y : x if x > y else y, nums))

def main():
    nums = [1,2,3,4,5]

    Data = Max(nums)

    print(Data)

if __name__ == "__main__":
    main()