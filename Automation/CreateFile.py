import os

def main():
    print("Enter name of the file that you want to create: ")
    Fname = input()

    open(Fname, "x")        #(file_name, mode)
                            # x indicates exclusive because we want to create file


if __name__ == "__main__":
    main()