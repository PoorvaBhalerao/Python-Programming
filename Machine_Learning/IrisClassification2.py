# Iris flower case study to predict whether the flower is of species Setosa,Virginica, Versicolor
from sklearn import tree # type: ignore
from sklearn.datasets import load_iris # type: ignore
from sklearn.model_selection import train_test_split # type: ignore


def main():
    print("--------Iris Flower Classification Case Study--------")

    iris = load_iris()

    print(iris)

    #print(type(iris))

    Features = iris.data
    Labels = iris.target

    data_train, data_test, target_train, target_test = train_test_split(Features, Labels, test_size= 0.5)  
                                                        # 0.5 indicates we have to split dataset in 50%





if __name__ == "__main__":
    main()