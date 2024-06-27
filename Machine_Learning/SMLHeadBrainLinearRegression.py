# There is one dataset which contains information about Head size and Brain weight.
# depends on gender and age.

# Consider below characteristic of Machine Learning Application:

# Classifier:                     Linear Regression
# DataSet:                        Head Brain Dataseet
# Features:                       Gender,Age,Head Size, Brain weight
# Labels:                         -
# Training DataSet:               237

import pandas as pd # type: ignore
from sklearn.linear_model import LinearRegression # type: ignore
from sklearn.metrics import mean_squared_error # type: ignore

def HeadBrainPredictor():

    #Load data
    data = pd.read_csv('HeadBrain.csv')

    print("Size of dataset: ",data.shape)

    X= data['Head Size(cm^3)'].values
    Y= data['Brain Weight(grams)'].values

    X = X.reshape((-1, 1))
    
    n = len(X)

    reg = LinearRegression()

    reg = reg.fit(X,Y)

    y_pred = reg.predict(X)

    r2 = reg.score(X,Y)

    print(r2)


def main():

    print("Supervised Machine Learning Application")

    print("Linear Regression on Head Brain size data set")

    HeadBrainPredictor()

if __name__ == "__main__":
    main()