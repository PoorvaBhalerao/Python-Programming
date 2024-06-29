# There is one dataset which contains information about Head size and Brain weight.
# depends on gender and age.

# Consider below characteristic of Machine Learning Application:

# Classifier:                     Linear Regression
# DataSet:                        Head Brain Dataseet
# Features:                       Gender,Age,Head Size, Brain weight
# Labels:                         -
# Training DataSet:               237
import numpy as np # type: ignore
import pandas as pd  # type: ignore
import matplotlib.pyplot as plt  # type: ignore

def HeadBrainPredictor():
    # Load data
    data = pd.read_csv('HeadBrain.csv')

    print("Size of dataset: ",data.shape)

    X= data['Head Size(cm^3)'].values
    Y= data['Brain Weight(grams)'].values

    # Least Square method
    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    n = len(X)

    numerator = 0
    demoninator = 0

    # Equation of line is y = mx + c

    for i in range(n):
        numerator += (X[i] - mean_x) * (Y[i] - mean_y)
        demoninator += (X[i] - mean_x)**2

    m = numerator / demoninator

    c = mean_y - (m * mean_x)

    print("Slope of Regression line is: ", m)
    print("Y intercept of Regression line is: ", c)

    max_x = np.max(X)+100
    min_x = np.min(X)-100

    #Display plotting of above points
    x = np.linspace(min_x, max_x, n)

    y = c + m*X

    plt.plot(x,y, color = '#58b970', label = 'Regression line')

    plt.scatter(X,Y, color = '#ef5423',label = 'Scatter plot')

    plt.xlabel('Head size in cm^3')

    plt.ylabel('Brain weight in gram')

    plt.legend()
    plt.show()

    #Findout goodness of fir ie R Square
    ss_t = 0
    ss_r = 0

    for i in range(n):
        y_pred = c + m*X
        ss_t += (Y[i] - mean_y)**2
        ss_r += (Y[i] - y_pred)**2

    r2 = 1- (ss_r/ss_t)

    print("R2 is:",r2)


def main():
    print("Supervised Machine Learning Application")

    print("Linear Regression on Head and Brain size dataset")

    HeadBrainPredictor()


if __name__ == "__main__":
    main()
