import sys

def main():
    print("Recursion limit is: ",sys.getrecursionlimit())   # 1000
# 1000 is default recursion limit in python3 
    sys.setrecursionlimit(1500)
    print("Recursion limit is: ",sys.getrecursionlimit())



if __name__ == "__main__":
    main()