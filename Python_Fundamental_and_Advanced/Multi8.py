# Accept number from user and display even or odd numbers on screen using threading
# when we enter large input which thread is sceduled and executed is not fixed 
# this desision is taken by thread sheduling algorithm of PVM.
import threading
import os

def DisplayEven(iNo):
    
    print("List of even numbers: ")
    x = 2
    for i in range(iNo):
        print("Even: ",x)
        x = x+2
    
def DisplayOdd(iNo):
    
    print("List of odd numbers: ")
    x = 1
    for i in range(iNo):
        print("Odd: ",x)
        x = x+2


def main():
        
    Value = int(input("Enter a number: "))

    p1 = threading.Thread(target = DisplayEven, args = (Value,))     # keyword arguments
    p2 = threading.Thread(target = DisplayOdd, args = (Value,))      # (value,) is tuple
    
    p1.start()      # process or thread is going from new to runnable
    p2.start()
    
    p1.join()    # join method does not allow controller till previous process is running
    p2.join()
    
    print("End of main thread")

    
if __name__ == "__main__":
    main()