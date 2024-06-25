# There is one dataset of advertisement agency
# dataset contains multiple records abour the customers whi=o invest in multiple advertisement options
# Depends on that sales features indicates the increased amount in there sales

# This data set contains 4 features as 
# TV
# Radio
# Television

# Depends on above three features Sales Feature indicates increassed sale amount.

# comsider below Characteristics of MachineLearning Algorithm:

# Classifier:                     Linear Regression
# DataSet:                        Advertisement Dataseet
# Features:                       TV,Radio,Television,Sales
# Labels:                         -

import pandas as pd # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.linear_model import LinearRegression # type: ignore
from sklearn.metrics import r2_score # type: ignore

def AdvertisementSales():

    #Load data
    data = pd.read_csv('Advertising.csv',index_col=0)

    print("Size of dataset: ",data.shape)

    # Seperate Features(X) and Labels(y)
    X = data[['TV','radio','newspaper']]
    y = data['sales']

    X_train,X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)# 80% for training and 20% for testing

    reg = LinearRegression()

    reg = reg.fit(X_train, y_train)

    y_pred = reg.predict(X_test)

    r2 = r2_score(y_test, y_pred)

    print("R-square: ",r2)


def main():

    print("Supervised Machine Learning Application")

    print("Linear Regression on Advertisement data set")

    AdvertisementSales()

if __name__ == "__main__":
    main()