# Write a program which accepts one number and display below pattern
# input 3
# 1   2   3 
# 1   2   3   
# 1   2   3

def Display(Num):
    a = 0
    for i in range(1,Num+1):
        for j in range(1,Num+1):
            print(j,end="  ")
            a = a+1 
              
        print("\n")


def main():
    A = int(input("Enter a Number: "))

    Display(A)
    



if __name__ == "__main__":
    main()