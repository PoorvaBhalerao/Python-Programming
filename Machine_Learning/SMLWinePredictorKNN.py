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

# Consider below Characteristics of Machine Learning Application:

# Classifier:                     K Nearest Neighbour
# DataSet:                        Wine Predictor DataSet
# Features:                       Alcohol, Malic Acid, Ash, Alcalinity of ash,
#                                 Magnesium, Total phenols, Flavanoids, 
#                                 Nonflavoured phenols, PRoanthocyanis,
#                                 color intensity, Hue, OD280/OD315 of diluted wines,
#                                 Proline                                                            
# Labels:                         Class1, Class2, Classs3
# Training Dataset:               70 % of 178 Entries
# Testing Dataset:                30 % of 178 Entries

from sklearn import metrics # type: ignore
from sklearn import datasets # type: ignore
from sklearn.neighbors import KNeighborsClassifier # type: ignore
from sklearn.model_selection import train_test_split # type: ignore

def WinePredictor():
    # Load dataset
    wine = datasets.load_wine()

    # print names of features
    print(wine.feature_names)

    # print label species(class_0, class_1, class_2)
    print(wine.target_names)

    # printthe wine data(top 5 records)
    print(wine.target[0:5])

    # print the wine labels(0: class_0, 1: class_1, 2: class_2)
    print(wine.target)

    X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3)#70 % training and 30 % testing

    # create KNNclassifier
    knn = KNeighborsClassifier(n_neighbors=3)

    # Train model using training sets
    knn.fit(X_train, y_train)

    # Predict the response for test dataset
    y_pred = knn.predict(X_test)

    print("Accuracy: ",metrics.accuracy_score(y_test, y_pred))


def main():
    print("Machine Learning Application")

    print("Wine predictor application using K Nearest NEighbour Algorithm")

    WinePredictor()

if __name__ == "__main__":
    main()