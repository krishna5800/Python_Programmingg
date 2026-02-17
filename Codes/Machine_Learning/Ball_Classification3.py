from sklearn import tree

def main():
    print("Ball Classifictaion Case Study")

    # Independent Variables
    Features = [[35, 1], [47, 1], [90, 0], [48, 1], [90, 0], [35, 1], [92, 0], [35, 1], [35, 1], [35, 1], [96, 0], [43, 1], [110, 0], [35, 1], [95, 0]]

    # Dependent Variabless
    Lables = [1, 1, 2, 1, 2, 1, 2, 1 , 1, 1, 2, 1, 2, 1, 2]

    modelobj = tree.DecisionTreeClassifier()

    trainedmodel = modelobj.fit(Features, Lables)

    Result  = trainedmodel.predict([[37, 1], [94, 0]])      # [1,2]

    print("Model predicts the object as : ",Result)

if __name__== "__main__":
    main()