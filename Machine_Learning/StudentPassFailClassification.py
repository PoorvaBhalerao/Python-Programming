#Student Pass orr Fail Classification Case Study
from sklearn.metrics import accuracy_score  # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.neighbors import KNeighborsClassifier  # type: ignore

def main():
    print("--------Student Pass orr Fail Classification Case Study--------")

    Features = [[4,3], [6,7], [7,8], [5,5], [8,8]]  # Featurs as marks in theory and Practical
    Labels = [0, 1, 1, 0, 1]    # 0 for fail and 1 for pass
    
    obj = KNeighborsClassifier(n_neighbors=3)
    
    obj.fit(Features, Labels)
   
    print(obj.predict([[9,5]])) #[1]Pass

    print(obj.predict([[6,6]])) #[1]Pass

    print(obj.predict([[3,5]])) #[0]Fail
    


if __name__ == "__main__":
    main()