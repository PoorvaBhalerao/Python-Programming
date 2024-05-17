# Design python application which creates two threads as evenfactor and oddfactor. 
# Both the thread accept one parameter as integer. Evenfactor thread will display 
# addition of even factors of given number and oddfactor will display addition of odd 
# factors of given number. After execution of both the thread gets completed main 
# thread should display message as “exit from main”.

import threading

def EvenFactor(Value):
    i = 0
    Sum = 0
    for i in range(2,Value):
        if((i%2 == 0) and (Value%i == 0)):
            Sum = Sum + i
    
    print("Addition of Even Factors:",Sum)


def OddFactor(Value):
    i = 0
    Sum = 0
    for i in range(1,Value):
        if((i%2 !=0) and (Value%i == 0)):
            Sum = Sum + i
    
    print("Addition of Odd Factors:",Sum)


def main():
    Value = int(input("Enter a number:"))

    p1 = threading.Thread(target=EvenFactor,args=(Value,))
    p2 = threading.Thread(target=OddFactor,args=(Value,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("End of main")


if __name__ == "__main__":
    main()
