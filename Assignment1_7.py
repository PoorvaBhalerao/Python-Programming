# Write a program which contains one function that accept one number from user 
# and returns true is number is divisible by 5 otherwise return false.

def Chk(No):
    if(No % 5 == 0):
        print("True")
        #print("Given number is divisible by 5")
    else:
        print("False")
        #print("Given number is not divisible by 5")
    
def main():
    print("Demonstration of Number divisibility By 5")
    print("Enter a number: ")
    A = int(input())
    
    Chk(A)



if __name__ == "__main__":
    main()