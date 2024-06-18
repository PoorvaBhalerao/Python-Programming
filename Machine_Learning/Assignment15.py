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
from sklearn.metrics import accuracy_score # type: ignore
from sklearn.neighbors import KNeighborsClassifier # type: ignore
from sklearn.tree import DecisionTreeClassifier # type: ignore
from sklearn.preprocessing import StandardScaler # type: ignore

data = pd.read_csv('WinePredictor.csv')

df = pd.DataFrame(data)
#print(data)

Features = df.drop('Class',axis=1)
#print(Features)
labels = df['Class'] 
#print(labels)

data_train, data_test, target_train, target_test = train_test_split(Features, labels, test_size=0.2)

# Standardize features by scaling them
#Standardize features by removing the mean and scaling to unit variance.
scaler = StandardScaler()
data_train_scaled = scaler.fit_transform(data_train)
data_test_scaled = scaler.transform(data_test)

knn = KNeighborsClassifier(n_neighbors=5)

# Train the model
knn.fit(data_train_scaled, target_train)

# Predictions on the test set
pred = knn.predict(data_test_scaled)

# Evaluate the model
accuracy = accuracy_score(target_test, pred)
print("Accuracy using K Nearest Neighbour algorithm is: ",accuracy*100,"%")


# obj = DecisionTreeClassifier()

# # Train the model
# obj.fit(data_train_scaled, target_train)

# # Predictions on the test set
# pred = obj.predict(data_test_scaled)

# # Evaluate the model
# accuracy = accuracy_score(target_test, pred)
# print("Accuracy using Decision tree algorithm is: ",accuracy*100,"%")