# Iris flower case study to predict whether the flower is of species Setosa,Virginica, Versicolor
from sklearn import tree # type: ignore
from sklearn.datasets import load_iris # type: ignore


def main():
    print("--------Iris Flower Classification Case Study--------")

    iris = load_iris()

    #print(iris)

    #print(type(iris))

    Features = iris.data
    Labels = iris.target

    print("Features are: ")
    print(Features)

    print("Labels are: ")
    print(Labels)





if __name__ == "__main__":
    main()