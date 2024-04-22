# def Addition(No1, No2, No3, No4):
#     pass

# #Result = Addition(10,20,30)        Error
# Result = Addition(10,20,30,40)
# print(Result)

def Addition(*No):
    
    Ans = 0
    print(type(No))
    print(len(No))
    
    for i in No:
        Ans = Ans + i
    
    return Ans

Result = Addition(10,20,30)
print(Result)

# Result = Addition(10,20,30,40)
# print(Result)

# Result = Addition(10,20,30,40,50)
# print(Result)
