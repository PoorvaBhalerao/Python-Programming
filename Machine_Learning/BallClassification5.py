# Ball Classification case study
# Detect the ball is tennis ball or Cricket ball
#Rough 1
#Smooth 0
#Tennis 1
#Cricket 2

from sklearn import tree # type: ignore

def MarvellousClassifier(weight, surface):
    # Feature Encoding
    Features = [[35, 1],[47, 1],[90, 0],[48, 1],[90, 0],[35, 1],[92, 0],[35, 1],[35, 1],[35, 1]]

    # Label Encoding
    Labels = [1, 1, 2, 1, 2, 1, 2, 1, 1, 1]

    # Decide the algorithm
    obj = tree.DecisionTreeClassifier()

    # Train the model
    obj = obj.fit(Features,Labels) 

    # Test the model
    ret = obj.predict([[weight, surface]])

    if ret == 1:
        print("Your object looks like Tennis ball")
    elif ret == 2:
        print("Your object looks like Cricket ball")
   


def main():
    print("----------Ball type classification case study----------")

    print("Please enter the information about the object that you want to test")
    
    print("Please enter weight of object in grams:")
    no = int(input())

    print("Please mention the type of surface Rough or Smooth: ")
    data = input()

    if data.lower() == "rough":
        data = 1
    elif data.lower() == "smooth":
        data = 0
    else:
        print("Invalid type of surface")
        exit()
        
    MarvellousClassifier(no, data)



if __name__ == "__main__":
    main()




    

    
    



