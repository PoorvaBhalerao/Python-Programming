# In this application we remove one entry from each Label of iris dataset and 
# train the model with remaining entries.
# And we apply predictions based on Decision tree with that removed entries

# Consider below characteristics of Machine Learning Apllication:

# Classifier:                 Decision Tree
# DataSet:                    Iris DataSet
# Features:                   Sepal Length, Sepal Width, Petal Length, Petal Width
# Labels:                     Versicolor, Setosa, Virginica
# Training Entries:           147 Entries
# Testing Dataset:            3 Entries

import numpy as np # type: ignore
from sklearn import tree # type: ignore
from sklearn.datasets import load_iris # type: ignore

iris = load_iris()

print("feature names of iris dataset:")
print(iris.feature_names)

print("Target names of iris dataset:")
print(iris.target_names)

#Indices of removed elements
test_index = [1,51,101]

#Training data with removed elements
train_target = np.delete(iris.target_names, test_index)
train_data = np.delete(iris.data, test_index, axis = 0)

#Test data for testing on training data
test_target = iris.target[test_index]
test_data= iris.data[test_index]

# form decision tree classifier
classifier = tree.DecisionTreeClassifier()

# Apply training data to form tree
classifier.fit(train_data, train_target)

print("values that we removed for testing")
print(test_target)

print("Result of testing")
print(classifier.predict(test_data))





