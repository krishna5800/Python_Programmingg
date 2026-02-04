
def AddPrime(List):
    Sum = 0
    Flag = False

    for i in List:
        Flag = False

        for j in range(2, i):
            if i % j == 0:
                Flag = True

        if Flag == False:
            Sum = Sum + i

    return Sum
