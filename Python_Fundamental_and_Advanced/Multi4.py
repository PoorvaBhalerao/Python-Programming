# Accept number from user and display even or odd numbers on screen using multiprocessing
import multiprocessing

def DisplayEven(iNo):
    print("List of even numbers: ")
    x = 2
    for i in range(iNo):
        print(x)
        x = x+2
    
def DisplayOdd(iNo):
    print("List of odd numbers: ")
    x = 1
    for i in range(iNo):
        print(x)
        x = x+2


def main():
    Value = int(input("Enter a number: "))

    p1 = multiprocessing.Process(target = DisplayEven, args = (Value,))     # keyword arguments
    p2 = multiprocessing.Process(target = DisplayOdd, args = (Value,))

    p1.start()
    p2.start()

    p1.join()       # due to . join() process main process will wait till 
    p2.join()       # its child process completely exuceted.

    print("End of main process")

    
if __name__ == "__main__":
    main()