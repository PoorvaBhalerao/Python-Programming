# Accuracy calculation with Decision Tree and K Nearest Neighbour
# In this applicaion we train iris dataset with Decision tree algorithm and K nearest Neighbour algorithm
# We divide iris dataset into two equal parts as trainig data and test data.
# We apply training on training data and predict the result on test data.
# We calculate accuracy of both algorithms by applying of test data.

# Consider below characteristics of Machine Learning Apllication:

# Classifier:                 Decision Tree and K Nearest Neighbour
# DataSet:                    Iris DataSet
# Features:                   Sepal Length, Sepal Width, Petal Length, Petal Width
# Labels:                     Versicolor, Setosa, Virginica
# Training Entries:           75 Entries
# Testing Dataset:            75 Entries

from sklearn import tree # type: ignore
from sklearn.datasets import load_iris # type: ignore
from sklearn.metrics import accuracy_score # type: ignore
from sklearn.neighbors import KNeighborsClassifier # type: ignore
from sklearn.model_selection import train_test_split # type: ignore

def CalculateAccuracyDecisionTree():
    iris = load_iris()
    #print(iris)
    data = iris.data
    target = iris.target

    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.5)

    classifier = tree.DecisionTreeClassifier()

    classifier.fit(data_train, target_train)

    predictions = classifier.predict(data_test)

    Accuracy = accuracy_score(target_test, predictions)

    return Accuracy


def CalculateAccuracyKNearestNeighbour():
    iris = load_iris()
    #print(iris)
    data = iris.data
    target = iris.target

    data_train, data_test, target_train, target_test = train_test_split(data, target, test_size = 0.5)

    classifier = KNeighborsClassifier()

    classifier.fit(data_train, target_train)

    predictions = classifier.predict(data_test)

    Accuracy = accuracy_score(target_test, predictions)

    return Accuracy

def main():
    Accuracy = CalculateAccuracyDecisionTree()
    print("Accuracy of classification algorithm with Decision Tree Classifier is: ",Accuracy*100,"%")

    Accuracy = CalculateAccuracyKNearestNeighbour()
    print("Accuracy of classification algorithm with K Nearest NEighbour Classifier is: ",Accuracy*100,"%")
    


if __name__ == "__main__":
    main()
