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

import pandas as pd  # type: ignore
from sklearn.neighbors import KNeighborsClassifier # type: ignore
from sklearn.tree import DecisionTreeClassifier # type: ignore 
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.preprocessing import OrdinalEncoder # type: ignore or OneHotEncoder is used here
from sklearn.metrics import accuracy_score # type: ignore


def CheckAccuracy():

    data = pd.read_csv("PlayPredictor.csv",index_col=0)

    print(data.head())

    # Convert categorical variables to numerical using One-Hot Encoding
    encoder = OrdinalEncoder()
    Features = encoder.fit_transform(data[['Whether', 'Temperature']])

    # Convert target variable 'play' to numerical
    Labels = data['Play'].apply(lambda x: 1 if x == 'Yes' else 0)

    print(data.head())

    data_train, data_test, target_train, target_test = train_test_split(Features, Labels, train_size=0.8)

    # knn = KNeighborsClassifier(n_neighbors=3)
    obj = KNeighborsClassifier()

    obj = obj.fit(data_train, target_train)

    predictions = obj.predict(data_test)
    #print(predictions)

    Accuracy = accuracy_score(target_test, predictions)

    return Accuracy

    
def main():
     
    Acc = CheckAccuracy()

    print("Accuracy of classification algorithm with K Nearest NEighbour Classifier is: ",Acc*100,"%")


if __name__ == "__main__":
    main()

