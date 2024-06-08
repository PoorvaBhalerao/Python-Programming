print("Demonstration of Functional")

Addition = lambda No1, No2: No1 + No2

Subtraction = lambda No1, No2: No1 - No2


print("Enter first number: ")
A = int(input())

print("Enter Second number: ")
B = int(input())

Ret = Addition(A, B)
print("Addition is: ",Ret)

Ret = Subtraction(A, B)
print("Subtraction is: ",Ret)


   
