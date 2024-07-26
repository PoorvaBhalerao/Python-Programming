import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from warnings import simplefilter

simplefilter(action='ignore', category=FutureWarning)

print("---------Diabetes Predictor using Decision Tree Algorithm---------------")

diabetes = pd.read_csv('diabetes.csv')

print("Columns of Dataset")
print(diabetes.columns)

print("First 5 records of dataset")
print(diabetes.head())

print("Diamension of diabetes data: {}".format(diabetes.shape))

X = diabetes.loc[:, diabetes.columns != 'Outcome']
y = diabetes['Outcome']

X_train, X_test, y_train, y_test = train_test_split( X, y, stratify=diabetes['Outcome'],random_state= 66)    

tree = DecisionTreeClassifier(random_state= 0)
tree.fit(X_train, y_train)

print("Accuracy on training set: {:.3f}".format(tree.score(X_train,y_train)))

print("Accuracy of testing set: {:.3f}".format(tree.score(X_test,y_test)))

tree = DecisionTreeClassifier(max_depth= 1, random_state= 0)
tree.fit(X_train, y_train)

print("Accuracy on training set: {:.3f}".format(tree.score(X_train,y_train)))

print("Accuracy of testing set: {:.3f}".format(tree.score(X_test,y_test)))

print("Feature importances:\n{}".format(tree.feature_importances_))

def plot_feature_importance_diabetes(model):
    plt.figure(figsize= (8,6))
    n_features = 8
    plt.barh(range(n_features), model.feature_importances_, align= 'center')
    diabetes_features = [X for i, X in enumerate(diabetes.columns) if i != 8]
    plt.yticks(np.arange(n_features), diabetes_features)
    plt.xlabel("feature importance")
    plt.xlabel("Features")
    plt.ylim(-1, n_features)
    plt.show()

plot_feature_importance_diabetes(tree)