# Design python application which creates two thread named as even and odd.
# Even thread will display first 10 even numbers and odd thread will display first 10 odd 
# numbers.

import threading

def DisplayEven():
    i = 0
    for i in range(2,21):
        if(i%2 == 0):
            print(i)

def DisplayOdd():
    i = 0
    for i in range(1,20):
        if(i%2 !=0):
            print(i)

def main():
    print("Demonstration of even and odd numbers")

    p1 = threading.Thread(target=DisplayEven)
    p2 = threading.Thread(target=DisplayOdd)

    p1.start()
    p2.start()

    p1.join()
    p2.join()



if __name__ == "__main__":
    main()

