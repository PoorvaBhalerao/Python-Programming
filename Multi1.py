import os


def main():
    print("PID of running process is : ",os.getpid())
    print("PID of parant process is ie command prompt is: ",os.getppid())


if __name__ == "__main__":
    main()