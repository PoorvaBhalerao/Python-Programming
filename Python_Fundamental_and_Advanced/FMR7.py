from functools import reduce

CheckEven = lambda No : (No % 2 == 0)
Increase = lambda No : No+1
Add = lambda A, B: A+B

# Task: Name of function
# Elements : List of data elements
#   filterX(CheckEven, [11,14,20,23,18,16,15,20]i.e. Data)
def filterX(Task, Elements):
    Result = []     # To store filtered data i e even numbers
    
    for no in Elements:
        Ret = Task(no)

        if(Ret == True):
            Result.append(no)
    
    return Result

#   mapX(Increase, FData)
def mapX(Task, Elements):
    Result = []     
    
    for no in Elements:
        Ret = Task(no)
        Result.append(Ret)
    
    return Result

def main():
    Data = [11,14,20,23,18,16,15,20]
    print("Data from input list: ",Data)

    
    FData = list(filterX(CheckEven, Data))  
    print("Data after filter function activity: ",FData)
    # 14    20  18  16  20

    
    MData = list(mapX(Increase, FData))
    print("Data after map function is: ",MData)
    # 15    21  19  17  21

    
    RData = reduce(Add, MData)
    print("Data after reduce activity is: ",RData)
    # 0 + 15    15
    # 15 + 21   36
    # 36 + 19   55
    # 55 + 17   72
    # 72 + 21    93



if __name__ == "__main__":
    main()