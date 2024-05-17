import os

def main():
    print("Enter name of the file that you want to create: ")
    Fname = input()

    if os.path.exists(Fname):
        print("Unable to create file as file is already exists")
    else:
        open(Fname, "x")        #(file_name, mode)
                                # x indicates exclusive because we want to create file
        print("File gets successfully created")

if __name__ == "__main__":
    main()

# Absolute path: C:\Users\admin\Desktop\Python\Automation/Marvellous.txt
# Relative path: Automation/Marvellous.txt