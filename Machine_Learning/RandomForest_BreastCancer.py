################################################################
# Required Python Packages
################################################################
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

#################################################################
# File Paths
##################################################
################
INPUT_PATH = "breast-cancer-wisconsin.data"
OUTPUT_PATH = "breast-cancer-wisconsin.csv"

#################################################################
# Headers
#################################################################
HEADERS = ["CodeNumber","ClumpThickness","UniformityCellSize","UniformityCellShape",
           "MarginalAdhesion", "SingleEpithelialCellSize","BareNuclei","BlandChromatin","NormalNucleoli","Mitoses",
           "CancerType"]

################################################################
# Function Name: read_data
# Description: Read the data into pandas dataframe
# Input: path of CSV file
# Output: Gives the data
# Author: Poorva Bhalerao
################################################################
def read_data(path):
    data = pd.read_csv(path)
    return data

################################################################
# Function Name: get_headers
# Description: dataset headers
# Input: dataset
# Output: Returns the header
# Author: Poorva Bhalerao
################################################################

def get_headers(dataset):
    return dataset.columns.values

################################################################
# Function Name: add_headers
# Description: Add the headers to dataset
# Input: dataset
# Output: Updated dataset
# Author: Poorva Bhalerao
################################################################

def add_headers(dataset, headers):
    dataset.columns = headers
    return dataset

################################################################
# Function Name: data_file_to_csv
# Input: Nothing
# Output: Write the data to CSV
# Author: Poorva Bhalerao
################################################################

def data_file_to_csv():
    # Headers
    headers = ["CodeNumber","ClumpThickness","UniformityCellSize","UniformityCellShape",
           "MarginalAdhesion", "SingleEpithelialCellSize","BareNuclei","BlandChromatin","NormalNucleoli","Mitoses",
           "CancerType"]
    
    # Load the dataser into Pandas data frame
    dataset = read_data(INPUT_PATH)
    # Add the headers to loaded dataset
    dataset = add_headers(dataset, headers)
    # Save the loaded dataset into csv format
    dataset.to_csv(T, index = False)
    print("File Saved...!")

################################################################
# Function Name: split_headers
# Description: Split the dataset with train_percentange
# Input: dataset with related information
# Output: dataset after splitting
# Author: Poorva Bhalerao
################################################################

def split_dataset(dataset, train_percentage, feature_headers, target_header):
    # Split dataset into train and test dataset
    train_x, test_x, train_y, test_y = train_test_split(dataset[feature_headers],
                                                        dataset[target_header], train_size=train_percentage)
    
    return train_x, test_x, train_y, test_y

################################################################
# Function Name: handel_missing_values
# Description: Filter missing values from the dataset
# Input: dataset with missing values
# Output: dataset by removing missing values
# Author: Poorva Bhalerao
################################################################

def handel_missing_values(dataset, missing_values_header, missing_label):
    return dataset[dataset[missing_values_header] != missing_label]

################################################################
# Function Name: random_forest_classifier
# Description: To train the random forest classifier with features and target data
# Author: Poorva Bhalerao
################################################################

def random_forest_classifier(features,target):
    clf = RandomForestClassifier()
    clf.fit(features, target)
    return clf

################################################################
# Function Name: dataset_statistic
# Description: Basic statistic of dataset
# Input: dataset 
# Output:Description of dataset
# Author: Poorva Bhalerao
################################################################

def dataset_statistic(dataset):
    print(dataset.describe())

################################################################
# Function Name: main
# Description: Main function from where execution starts
# Author: Poorva Bhalerao
################################################################

def main():
    #Lead the csv file into pandas dataframe
    dataset = pd.read_csv(OUTPUT_PATH)
    # Get basic statistic of leaded dataset
    dataset_statistic(dataset)

    #Filter missing values
    dataset = handel_missing_values(dataset, HEADERS[6], '?')
    train_x, test_x, train_y, test_y = split_dataset(dataset, 0.7, HEADERS[1:-1], HEADERS[-1])

    # Train and Test dataset size details
    print("Train_x Shape::", train_x.shape)
    print("Train_y Shape::", train_y.shape)
    print("Test_x Shape::", test_x.shape)
    print("Test_y Shape::", test_y.shape)

    #Create random forest classifier instance
    trained_model = random_forest_classifier(train_x, train_y)
    print("Trained model:: ",trained_model)
    predictions = trained_model.predict(test_x)

    for i in range(0, 205):
        print("Actual outcone:: {} and Predicted outcome :: {}".format(list(test_y)[i], predictions[i]))

    print("Train_accuracy::",accuracy_score(train_y, trained_model.predict(train_x)))
    print("Test Accuracy::",accuracy_score(test_y, predictions))
    print("Confusion matrix::",confusion_matrix(test_y, predictions))

######################################################################
# Application Starter
#####################################################################
if __name__ == "__main__":
    main()
