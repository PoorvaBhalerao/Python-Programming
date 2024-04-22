# Write a program which accepts one number and display below pattern
# input 3
# 1   
# 1   2     
# 1   2   3

def Display(Num):
    if Num<=0:
        print("Pls enter a Positive number greter than zero")
    else:
        for i in range(1, Num+1):
            for j in range(1,i+1):
                print(j,end="   ")
            print()


def main():
    A = int(input("Enter a Number: "))

    Display(A)
    



if __name__ == "__main__":
    main()
