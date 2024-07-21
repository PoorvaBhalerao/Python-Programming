import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

print("--------------Disbetes Predictor using K nearest neighbour------------")

diabetes = pd.read_csv('diabetes.csv')
print(diabetes)

print("Columns of Dataset")
print(diabetes.columns)

print("First 5 records of dataset")
print(diabetes.head())

print("Dimension of diabetes data: {}".format(diabetes.shape))

X = diabetes.loc[:, diabetes.columns != 'Outcome']
y = diabetes['Outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify= diabetes['Outcome'],random_state=66)

training_accuracy = []
test_accuracy = []

# try n_neighbors from 1 to 10
neighbors_setting = range(1, 11)

for n_neighbors in neighbors_setting:
    # build the model
    knn = KNeighborsClassifier(n_neighbors= n_neighbors)
    knn.fit(X_train, y_train)
    # record training set accuracy
    training_accuracy.append(knn.score(X_train, y_train))
    # record test set accuracy
    test_accuracy.append(knn.score(X_test, y_test))

plt.plot(neighbors_setting, training_accuracy, label = "training accuracy")
plt.plot(neighbors_setting, test_accuracy, label = "test accuracy")
plt.ylabel("Accuracy")
plt.xlabel("n_neighbors")
plt.legend()
plt.savefig('knn_compare_model')
plt.show()

knn = KNeighborsClassifier(n_neighbors= 9)

knn.fit(X_train, y_train)

print("Accuracy of KNN Classifier on training set: {:.2f}".format(knn.score(X_train, y_train)))

print("Accuracy of KNN classifier on test set: {:.2f}".format(knn.score(X_test,y_test)))

