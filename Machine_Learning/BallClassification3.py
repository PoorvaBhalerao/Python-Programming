#Ball Classification case study
#Rough 1
#Smooth 0
#Tennis 1
#Cricket 2

from sklearn import tree # type: ignore

import sklearn # type: ignore

def main():
    print("Ball Classification case study")

    # Feature Encoding
    Features = [[35, 1],[47, 1],[90, 0],[48, 1],[90, 0],[35, 1],[92, 0],[35, 1],[35, 1],[35, 1]]

    # Label Encoding
    Labels = [1, 1, 2, 1, 2, 1, 2, 1, 1, 1]

    # Decide the algorithm
    obj = tree.DecisionTreeClassifier()

    # Train the model
    obj = obj.fit(Features, Labels)     # fit() method is used to train the model

    # Test the model
    print(obj.predict([[96,0]]))
    print(obj.predict([[43,1]]))




if __name__ == "__main__":
    main()

