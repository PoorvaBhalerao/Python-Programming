# There is dataset of wine which classify the wines according to its contents into three classes.
# These data are result of chemical analysis of wines grown in same resion in Italy
# but derived from three different cultivars, The analysis determined the quantities of 13
# constituents found in each of the three types of WindowsError

# Wine dataset contains 13 features as

# 1. Alcohol
# 2. Malic Acid
# 3. Ash
# 4. Alcalinity of ash
# 5. Magnesium
# 6. Total phenols
# 7. Flavanoids
# 8. Nonflavanoid phenols
# 9. Proanthocyanins
# 10. Color intensity
# 11. Hue
# 12. OD280/OD315 of diluted Wines
# 13. Proline

# According to above features wine can be classified as
# 1. Class 1
# 2. Class 2
# 3. Class 3

import pandas as pd # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.preprocessing import StandardScaler # type: ignore
from sklearn.neighbors import KNeighborsClassifier # type: ignore
from sklearn.metrics import accuracy_score # type: ignore


def CheckAccuracy():
    file_path = 'WinePredictor.csv'
    wine_df = pd.read_csv(file_path)

    print(wine_df.head())

    X = wine_df.drop('Class', axis=1)
    y = wine_df['Class']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    knn = KNeighborsClassifier(n_neighbors=3)  
    knn.fit(X_train, y_train)

    y_pred = knn.predict(X_test)

    return accuracy_score(y_test, y_pred)

def main():
    
    iRes=CheckAccuracy()
    
    print("Accuracy is:",iRes*100,"%")
    
if __name__=="__main__":
    main()