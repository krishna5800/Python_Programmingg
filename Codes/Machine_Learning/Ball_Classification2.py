import sklearn

# Rough :   1
# Smooth :  0

# Tennis :  1
# Cricket : 2

def main():
    print("Ball Classifictaion Case Study")

    # Data Loading

    # Replaced Rough with 1 and Smooth with 0 --> Encoding
    # Feature Encoding
    Features = [[35, 1], [47, 1], [90, 0], [48, 1], [90, 0], [35, 1], [92, 0], [35, 1], [35, 1], [35, 1], [96, 0], [43, 1], [110, 0], [35, 1], [95, 0]]

    # Replace Tennis with 1 and Cricket with 2 --> Encoding
    # Lable Encoding
    Lables = [1, 1, 2, 1, 2, 1, 2, 1 , 1, 1, 2, 1, 2, 1, 2]

    

if __name__== "__main__":
    main()

# Dataset Size : 15