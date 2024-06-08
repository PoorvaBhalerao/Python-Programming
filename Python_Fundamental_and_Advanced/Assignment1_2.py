# Write a program which contains one function named as ChkNum() which accepts one
# parameter as number if number is even it should display "Even number"
# other wise "Odd number" on console

def ChkNum(Num):
    if(Num % 2 == 0):
        print("Even number")
    else:
        print("Odd number")
    
def main():
    print("Demonstration of Even or Odd number")
    A = int(input("Enter a Number:  "))
    
    ChkNum(A)


if __name__ == "__main__":
    main()
