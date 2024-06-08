import sys

def main():
    print("Demonstration of command line arguments")
    print("Name of application: ",sys.argv[0])      #Command.py(files name)
    print("Datatype of argv is: ",type(sys.argv))       #<class 'list'>
    print("No of command line arguments are: ",len(sys.argv))      # 1 because file name is oth command line argument


        
    
if __name__ == "__main__":
    main()