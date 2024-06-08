from functools import reduce


#CheckEven = lambda No:(No%2 == 0)


#Increase = lambda No: No+1


#Add =lambda A, B: A+B




def main():
    Data = [11,14,20,23,18,16,15,20]
    print("Data from input list: ",Data)

    # filter function has to be give 1st parameter which gives return value True or false
    #FData = list(filter(CheckEven, Data))   # filter(what to do function, our data)
    FData = list(filter(lambda No:(No%2 == 0), Data))
    print("Data after filter function activity: ",FData)
    # 14    20  18  16  20

    # map function has to be given 1 st parameter which gives return to operation
    #MData = list(map(Increase, FData))
    MData = list(map(lambda No: No+1, FData))
    print("Data after map function is: ",MData)
    # 15    21  19  17  21

    # reduce function has to give two parameters whose gives operation of that two numbers and give one output
    #RData = reduce(Add, MData)
    RData = reduce(lambda A, B: A+B, MData)
    print("Data after reduce activity is: ",RData)
    # 0 + 15    15
    # 15 + 21   36
    # 36 + 19   55
    # 55 + 17   72
    # 72 + 21    93



if __name__ == "__main__":
    main()