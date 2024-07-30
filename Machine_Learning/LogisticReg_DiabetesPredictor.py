import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from warnings import simplefilter

simplefilter(action='ignore', category=FutureWarning)

print("---------Diabetes Predictor using Logistic Regression---------------")

diabetes = pd.read_csv('diabetes.csv')

print("Columns of Dataset")
print(diabetes.columns)

print("First 5 records of dataset")
print(diabetes.head())

print("Diamension of diabetes data: {}".format(diabetes.shape))

X = diabetes.loc[:, diabetes.columns != 'Outcome']
y = diabetes['Outcome']

X_train, X_test, y_train, y_test = train_test_split( X, y, stratify=diabetes['Outcome'],random_state= 66)    

logreg = LogisticRegression().fit(X_train,y_train)

print("Traning set accuracy: {:.3f}".format(logreg.score(X_train, y_train)))

print("Testing set accuracy: {:.3f}".format(logreg.score(X_test,y_test)))

logreg001 = LogisticRegression(C=0.001).fit(X_train, y_train)

print("Traning set accuracy: {:.3f}".format(logreg001.score(X_train, y_train)))
print("Testing set accuracy: {:.3f}".format(logreg001.score(X_test,y_test)))
