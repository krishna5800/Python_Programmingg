import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():

    # Load the data

    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Value of Independent variables : ", X)
    print("Value of Dependent variables : ", Y)

    mean_X = np.mean(X)
    mean_Y = np.mean(Y)

    print("X mean is : ", mean_X)
    print("Y mean is : ", mean_Y)

def main():
    
    MarvellousPredictor()

if __name__ == "__main__":
    main()