import sys

def main():
    print("Demonstration of addition using command line argument")
    print("Addition of two numbers is:  ",int(sys.argv[1])+int(sys.argv[2]))

if __name__ == "__main__":
    main()