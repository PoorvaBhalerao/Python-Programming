# Accept number from user and display even or odd numbers on screen using multiprocessing
# PID are different because these are seperate processes

import multiprocessing
import os

def DisplayEven(iNo):
    print("PID of even process: ",os.getpid())
    print("List of even numbers: ")
    x = 2
    for i in range(iNo):
        print(x)
        x = x+2
    
def DisplayOdd(iNo):
    print("PID of odd process: ",os.getpid())
    print("List of odd numbers: ")
    x = 1
    for i in range(iNo):
        print(x)
        x = x+2


def main():
    print("PID of main process: ",os.getpid())
    Value = int(input("Enter a number: "))

    p1 = multiprocessing.Process(target = DisplayEven, args = (Value,))     # keyword arguments
    p2 = multiprocessing.Process(target = DisplayOdd, args = (Value,))      # (value,) is tuple

    p1.start()      # this is not good way of multiprocessing
    p1.join()       # due to this parellel execution is not working

    p2.start()      # first p1 is executed and then p2
    p2.join()       # see previous code there is parellel execution

    print("End of main process")

    
if __name__ == "__main__":
    main()