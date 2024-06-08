#Ball Classification case study
#Use of encoding

#Rough 1
#Smooth 0

#Tennis 1
#Cricket 2

import sklearn # type: ignore

def main():
    print("Ball Classification case study")

    # Feature Encoding
    Features = [[35, 1],[47, 1],[90, 0],[48, 1],[90, 0],[35, 1],[92, 0],[35, 1],[35, 1],[35, 1]]

    # Label Encoding
    Labels = [1, 1, 2, 1, 2, 1, 2, 1, 1, 1]


if __name__ == "__main__":
    main()

# Dataset Size: 15  (Total size)
# Training Size: 10 (see above 10 datasets)
# Testing Size: 5   (We set for testing only 5 datasets)