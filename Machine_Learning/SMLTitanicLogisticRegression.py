# There is a dataset which contains information about passengers from Titanic
# This data set descibe multiple features about survived and non survived passengers
# comsider below Characteristics of MachineLearning Algorithm:

# Classifier:                     Logistic Regression
# DataSet:                        titanic Dataseet
# Features:                       Passenger id, Gender, Age, Fare, Class etc
# Labels:                         -

import math
import numpy as np # type: ignore
import pandas as pd # type: ignore
import seaborn as sns # type: ignore
from seaborn import countplot # type: ignore
import matplotlib.pyplot as plt # type: ignore
from matplotlib.pyplot import figure,show # type: ignore
from sklearn.metrics import accuracy_score,confusion_matrix, classification_report # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.linear_model import LogisticRegression # type: ignore

def TitanicLogistic():
    # Step1 : Load data
    titanic_data = pd.read_csv('TitanicDataset.csv')

    print("First 5 entries from loaded dataset:")
    print(titanic_data.head())

    print("Number of Passengers are "+str(len(titanic_data)))

    # Step2 : Analyze data
    print("Visualisation: Survived and non survived passengers:")
    figure()
    target = "Survived"

    countplot(data = titanic_data, x = target).set_title("Survived and Non Survied Passengers")
    show()

    print("Visualisation: Survived and non survived passengers based on Gender")
    figure()
    target = "Survived"

    countplot(data = titanic_data, x = target, hue ="Sex").set_title("Survived and non survied passengers based on GEnder")
    show()

    print("Visualisation: Survived and non survived passengers based on the PAssenger class")
    figure()
    target = "Survived"

    countplot(data = titanic_data, x = target, hue ="Pclass").set_title("Survived and non survied passengers based on Passenger class")
    show()

    print("Visualisation: Survived and non survived passengers based on Age")
    figure()
    titanic_data["Age"].plot.hist().set_title("Survived and non Survived based on Age")
    show()

    print("Visualisation: Survived and non survived passengers based on fare")
    figure()
    titanic_data["Fare"].plot.hist().set_title("Survived and non Survived based on Fare")
    show()

    #Step3: Data Cleaning

    titanic_data.drop("zero",axis = 1, inplace = True)

    print("First 5 entries from loaded dataset after removing zero column:")
    print(titanic_data.head(5))

    print("Values of Sex column")
    print(pd.get_dummies(titanic_data["Sex"]))

    print("Values of sex column after removing one field:")
    print(pd.get_dummies(titanic_data["Sex"], drop_first = True))
    print(titanic_data["Sex"].head(5))

    print("Values of PClass column after removing one field:")
    print(pd.get_dummies(titanic_data["Pclass"], drop_first = True))
    print(titanic_data["Pclass"].head(5))

    print("Values of dataset after concstenating new columns:")
    titanic_data = pd.concat([titanic_data,titanic_data["Sex"],titanic_data["Pclass"]], axis = 1)
    print(titanic_data.head(5))

    print("Values of dataset after removing irrelevent columns:")
    titanic_data.drop(["Sex","sibsp","Parch","Embarked"], axis = 1, inplace = True)
    print(titanic_data.head(5))

    x = titanic_data.drop("Survived", axis = 1)
    y = titanic_data["Survived"]

    #Step 4 : Data Training
    xtrain, xtest, ytrain, ytest = train_test_split(x,y, test_size = 0.5)

    logmodel = LogisticRegression()

    logmodel.fit(xtrain, ytrain)

    #Step4: Data Testing
    prediction = logmodel.predict(xtest)

    #step5: Calculate Accuracy
    print("Classification report of Logistic Regression is:")
    print(classification_report(ytest, prediction))

    print("Confusion Matrix of Logistic Regression is:")    # PN PY AN AY
    print(confusion_matrix(ytest, prediction))

    print("Accuracy of Logistic Regression is: ")
    print(accuracy_score(ytest, prediction))

def main():
    print("Supervised Machine Learning")

    print("Logistic Regression on titanis data set")

    TitanicLogistic()

if __name__ == "__main__":
    main()
    

