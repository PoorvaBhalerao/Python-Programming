import os
import multiprocessing

def Task1(No):
    print("Executing first task")
    print("PID of task1: ",os.getpid())             # imaginary 51
    print("PPID of task1: ",os.getppid())           # 11

def Task2(No):
    print("Executing second task")
    print("PID of task2: ",os.getpid())             # imaginary 101
    print("PPID of task2: ",os.getppid())           # 11



def main():
    print("PID of running process is : ",os.getpid())                       # imaginary 11
    print("PID of parant process is ie command prompt is: ",os.getppid())   # imaginary 21

    Value = 11
    p1 = multiprocessing.Process(target = Task1, args = (Value,))   # we are passing tuple in args
    p2 = multiprocessing.Process(target = Task2, args = (Value,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    main()