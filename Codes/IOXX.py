# By defauly input() accepts data in str datatype so do typecasting

print("Enter first Number : ")
No1 = input()

print("Enter second Number : ")
No2 = input()

print(type(No1))
print(type(No2))

Ans = int(No1) + int(No2)

print(type(No1))
print(type(No2))

print("Addition is : ",Ans)