import os

def main():
    print("Enter name of the file that you want to open for reading purpose: ")
    Fname = input()

    if os.path.exists(Fname):
        fobj = open(Fname, "r")     # r for read
        print("File is successfully opened in read mode")

        for line in fobj:
            print(line)

        fobj.close()
                    
    else:
        print("Unable to open file as file is not present in current directory")

if __name__ == "__main__":
    main()

