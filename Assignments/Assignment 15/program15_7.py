# 7. Write a lambda function using filter() which accepts a list of strings and returns 
# a list of strings having length greater than 5

StringGreat = lambda nums : list(filter(lambda No : len(No) > 5, nums))


def main():
    nums = ["Krishna", "Tanya", "Pan", "Yuvraj"]

    Data = StringGreat(nums)

    print(Data)

if __name__ == "__main__":
    main()