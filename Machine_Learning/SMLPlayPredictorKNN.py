# Weather condition dataset
# This Dataset contains information of weather and whether to Play or not.
# Data set contains target variable as Play which indicates whether to play or not.
# Dataset has two features as
# 1. weather
# 2. Temperature

# We have to Labels as
# 1. Yes
# 2. No

# There are three types of entries under weather as 
# 1. Sunny
# 2. Overcast
# 3. Rainy

# There are three types of different entries under Temperature as 
# 1. Hot
# 2. Cold
# 3. Mild

# Consider below Characteristics of Machine Learning Application:

# Classifier:                     K Nearest Neighbour
# DataSet:                        Play Predictor DataSet
# Features:                       Whether, Temperature
# Labels:                         Yes, No 
# Training Dataset:               30 Entries
# Testing Dataset:                1 Entry

import numpy as np # type: ignore
import pandas as pd # type: ignore
from sklearn import preprocessing # type: ignore
from sklearn.neighbors import KNeighborsClassifier # type: ignore

def PlayPredictor(data_path):
    #Step 1 : Load data
    data = pd.read_csv(data_path)

    print("Size of Actual dataset:", len(data))

    #Step 2 : Clean ,Prepare and Manipulate data
    feature_names = ['Whether', 'Temperature']

    print("Names of Features: ", feature_names)

    Whether = data.Whether
    Temperature = data.Temperature
    Play = data.Play

    #creating labelEncoder
    le = preprocessing.LabelEncoder()

    #Converting string labels into numbers
    whether_encoded = le.fit_transform(Whether)
    print('Whether:',whether_encoded)

    #Converting string labels into numbers
    temperature_encoded = le.fit_transform(Temperature)
    print('Temperature:',temperature_encoded)

    label = le.fit_transform(Play)
    print('label:',label)

    #Combile whether and temperature into single listof tuples
    features = list(zip(whether_encoded, temperature_encoded))

    #Step 3 : Train Data
    model = KNeighborsClassifier(n_neighbors=3)

    #Train model using training sets
    model.fit(features, label) 

    #Step 4 : Test data
    predicted = model.predict([[0,2]])  #0: Ovaercast , 2: Mild
    if(predicted == 1):
        print(predicted)
        print("You can Play")
    else:
        print(predicted)
        print("You cannot play")
        


def main():
    print("Supervised Machine Learning Application")

    print("Play Predictor application using K Nearest Neighbour algoritthm")

    PlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()