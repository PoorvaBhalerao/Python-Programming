# Wrire a program which accepts file name from user and create new file named as Demo.txt and copy all the contents from existing file into new file. Accept file name through command line arguments
# Input: ABC.txt
# Create new file as ABC.txt and copy contents of Demo.txt to ABC.txt

import os

def main():
    Fname1 = print("Enter the file name you want to create and open:")

    if os.path.exists(Fname1):
        print("Unable to create file as file is already exits")

    else:
        open(Fname1, 'x')
        print("File gets succesfully created")

    Fname = input("Enter the file name you want to open:")

    with open(Fname,'r') as firstfile, open(Fname1,'w') as secondfile: 
    # read content from first file 
        for line in firstfile: 
            # write content to second file 
            secondfile.write(line)
    
    fobj = open(Fname1, 'r')

    Data = fobj.read()
    print("The copied data is: ",Data)

    fobj.close()
    

if __name__ == "__main__":
    main()