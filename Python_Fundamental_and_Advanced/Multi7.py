# Accept number from user and display even or odd numbers on screen using threading
# PID are same because it is single process but TID are different because these are multiple thereds
import threading
import os

def DisplayEven(iNo):
    print("PID of even process: ",os.getpid())
    print("TID of even thread ",threading.get_ident())
    print("List of even numbers: ")
    x = 2
    for i in range(iNo):
        print(x)
        x = x+2
    
def DisplayOdd(iNo):
    print("PID of odd process: ",os.getpid())
    print("TID of odd thread ",threading.get_ident())
    print("List of odd numbers: ")
    x = 1
    for i in range(iNo):
        print(x)
        x = x+2


def main():
    print("PID of main process: ",os.getpid())
    print("TID of main thread ",threading.get_ident())
    
    Value = int(input("Enter a number: "))

    p1 = threading.Thread(target = DisplayEven, args = (Value,))     # keyword arguments
    p2 = threading.Thread(target = DisplayOdd, args = (Value,))      # (value,) is tuple

    p1.start()      
    p2.start()
    
    p1.join()    
    p2.join()       
    
    print("End of main thread")

    
if __name__ == "__main__":
    main()