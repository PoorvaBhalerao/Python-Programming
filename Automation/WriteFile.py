import os

def main():
    print("Enter name of the file that you want to open for writing purpose: ")
    Fname = input()

    if os.path.exists(Fname):
        fobj = open(Fname, "w")     # w for write
        print("File is successfully opened in write mode")

        print("Enter data that you want to write in file:")
        Data = input()

        fobj.write(Data)
        
                    
    else:
        print("Unable to open file as file is not present in current directory")

if __name__ == "__main__":
    main()

