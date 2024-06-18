# Iris dataset contains information of flowers under Iris family.
# There are three types of flowers.
# 1. Iris Versicolor
# 2. Iris Setosa
# 3. Iris Virginica
# The dataset contains 4 features as Sepal Length, Sepal Width, Petal Length, Petal Width
# Thae Dataset contains 150 records
# Consider below characteristics of Machine Learning Application:

# Classifier:                 Decision Tree
# DataSet:                    Iris DataSet
# Features:                   Sepal Length, Sepal Width, Petal Length, Petal Width
# Labels:                     Versicolor, Setosa, Virginica
# Training Entries:           150 Entries
# Testing Dataset:            -

# Consider below Application which loads Iris dataset and display all records and labels of that Dataset

from sklearn.datasets import load_iris # type: ignore

iris = load_iris()

#print(iris)

print("Feature names of iris data set:")
print(iris.feature_names)

print("Target names of iris data set:")
print(iris.target_names)

for i in range(len(iris.target)):       #range(0,150)
    print("ID: %d, Label: %s, Feature: %s"%(i,iris.data[i],iris.target[i]))

