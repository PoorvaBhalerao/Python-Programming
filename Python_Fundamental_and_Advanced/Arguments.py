# Types of function arguments
# 1 Positional Arguments
# 2 Keyword Arguments
# 3 Default Arguments
# 4 Variable number of Arguments

# 1 Positional Arguments

def Information(Name, Age, Salary):
    print("Name is: ", Name)
    print("Age is: ", Age)
    print("Salary is: ", Salary)

Information("Poorva", 28, 70000)
Information("Rohan", 33, 100000)

# 2 Keyword Arguments

Information(Age = 29, Salary = 50000, Name = "Rutuja")