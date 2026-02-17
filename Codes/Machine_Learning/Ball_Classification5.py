from sklearn import tree

def main():
    print("Ball Classifictaion Case Study")

    # Original Encoded Dataset

    # Independent Variables
    X = [[35, 1], [47, 1], [90, 0], [48, 1], [90, 0], [35, 1], [92, 0], [35, 1], [35, 1], [35, 1], [96, 0], [43, 1], [110, 0], [35, 1], [95, 0]]

    # Dependent Variabless
    Y = [1, 1, 2, 1, 2, 1, 2, 1 , 1, 1, 2, 1, 2, 1, 2]

    # Independent variables for training 
    X_train = [[35, 1], [47, 1], [90, 0], [48, 1], [90, 0], [35, 1], [92, 0], [35, 1], [35, 1], [35, 1], [96, 0], [43, 1], [110, 0]]

    # Independent variables for testing 
    X_test = [[35, 1], [95, 0]]

    # Dependent variables for training 
    Y_train = [1, 1, 2, 1, 2, 1, 2, 1 , 1, 1, 2, 1, 2]

    # Dependent variables for testing
    Y_test = [1, 2]

    modelobj = tree.DecisionTreeClassifier()

    trainedmodel = modelobj.fit(X_train, Y_train)

    Result  = trainedmodel.predict(X_test)   

    print("Model predicts the object as : ",Result)

if __name__== "__main__":
    main()