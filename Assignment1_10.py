# Write a program which accepts name from user and
# display length of its name

def DispLen(Name):
    Size = 0
    for i in Name:
        Size = Size +1
    return Size
    # B = len(Name)
    # return B        


def main():
    print("Demonstration of the Length of Word")
    a = list(input("Enter Your Name: "))
    Ret = 0
    
    Ret = DispLen(a)
    
    print("Length of name is: ", Ret)
    



if __name__ == "__main__":
    main()