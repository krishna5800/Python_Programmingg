from sklearn.metrics import confusion_matrix

def main():
    # Positive : 1
    # Negative : 0

    Actual =    [1,0,1,1,1,0,1,0,0,1]
    Predicted = [1,0,0,1,1,1,1,1,0,1]

    print("Actual data : ", Actual)
    print("Predicted data : ", Predicted)

    Con_Mat = confusion_matrix(Actual, Predicted)

    print(Con_Mat)

if __name__ == "__main__":
    main()