# 8. Write a lambda function using filter() which accepts a list of numbers and returns a
# list of numbers divisible by both 3 and 5.

Divisible = lambda nums : list(filter(lambda No : No%3 == 0 and No%5 == 0, nums))

def main():
    nums = [1,3,15,5]

    Data = Divisible(nums)

    print(Data)

if __name__ == "__main__":
    main()