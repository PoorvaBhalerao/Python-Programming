from functools import reduce


def CheckEven(No):
    return (No%2 == 0)

def Increase(No):
    return No+1

def Add(A, B):
    return A+B




def main():
    Data = [11,14,20,23,18,16,15,20]
    print("Data from input list: ",Data)

    FData = list(filter(CheckEven, Data))   # filter(what to do function, our data)
    print("Data after filter function activity: ",FData)

    MData = list(map(Increase, FData))
    print("Data after map function is: ",MData)

    RData = reduce(Add, MData)
    print("Data after reduce activity is: ",RData)



if __name__ == "__main__":
    main()