#Ball Classification case study

import sklearn # type: ignore

def main():
    print("Ball Classification case study")

    Features = [[35, "Rough"],[47, "Rough"],[90, "Smooth"],[48, "Rough"],[90, "Smooth"]
                ,[35, "Rough"],[92, "Smooth"],[35, "Rough"],[35, "Rough"],[35, "Rough"]]

    Labels = ["Tennis", "Tennis", "Cricket", "Tennis", "Cricket",
               "Tennis", "Cricket", "Tennis", "Tennis", "Tennis"]


if __name__ == "__main__":
    main()

# Dataset Size: 15  (Total size)
# Training Size: 10 (see above 10 datasets)
# Testing Size: 5   (We set for testing only 5 datasets)