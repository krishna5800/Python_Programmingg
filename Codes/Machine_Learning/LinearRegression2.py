import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():

    # Load the data

    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Value of Independent variables : ", X)
    print("Value of Dependent variables : ", Y)

    mean_X = np.mean(X) # 3.0
    mean_Y = np.mean(Y) # 3.6

    print("X mean is : ", mean_X)
    print("Y mean is : ", mean_Y)

    n = len(X)  # 5

    # Y = mX + C

    # m = (summation of (X - mean_X) * (Y - mean_Y) / (summation of (X - mean_X)) ** 2) 

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i] - mean_X) * (Y[i] - mean_Y))
        denominator = denominator + ((X[i] - mean_X) ** 2)

    m = numerator / denominator

    print("Slope of line i.e. m : ", m)    # 0.4

    C = mean_Y - (m * mean_X)

    print("Y intercept of line is i.e. C : ", C)

def main():
    
    MarvellousPredictor()

if __name__ == "__main__":
    main()