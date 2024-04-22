# Write a program which accept one number for user and check whether number is prime or not

def ChkPrime(Num):
    flag = True
    if Num == 1:
        print(Num," is the prime number")
    elif(Num > 1):
        for i in range(2,Num):
            if((Num % i) == 0):
                flag = False
                break
            
    if (flag == True):
        print("it is not a prime number")
    else:
        print("It is a prime number")



def main():
    print("Demonstration of Number is Prime or Not")
    A = int(input("Enter a number:  "))

    ChkPrime(A)




if __name__ == "__main__":
    main()