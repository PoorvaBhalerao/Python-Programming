# Whether condition dataset
# This Dataset contains information of Whether and whether to Play or not.
# Data set contains target variable as Play which indicates whether to play or not.
# Dataset has two features as
# 1. Whether
# 2. Temperature

# We have to Labels as
# 1. Yes
# 2. No

# There are three types of entries under Whether as 
# 1. Sunny
# 2. Overcast
# 3. Rainy

# There are three types of different entries under Temperature as 
# 1. Hot
# 2. Cold
# 3. Mild

import pandas as pd # type: ignore
from sklearn.preprocessing import LabelEncoder # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.neighbors import KNeighborsClassifier # type: ignore
from sklearn.metrics import accuracy_score # type: ignore


def CheckAccuracy():
    # file_path = 'PlayPredictor.csv'  
    # data = pd.read_csv(file_path)
    data = pd.read_csv("PlayPredictor.csv",index_col=0)

    print(data.head())


    label_encoder = LabelEncoder()


    data['Whether'] = label_encoder.fit_transform(data['Whether'])


    data['Temperature'] = label_encoder.fit_transform(data['Temperature'])


    print("\nTransformed Dataset:")
    print(data.head())


    X = data[['Whether', 'Temperature']]
    y = data['Play']  


    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.5)


    knn = KNeighborsClassifier(n_neighbors=3)  
    knn.fit(X_train, y_train)
    y_pred_knn = knn.predict(X_test)

    return accuracy_score(y_test, y_pred_knn)
    

def main():
    
    iRes=CheckAccuracy()
    
    print("Accuracy is:",iRes)
    
if __name__=="__main__":
    main()
