# Write a program which accepts one number fron user and return addition of its factors.

def AddFact(Num):
    Fact = 0
    for i in range(1, Num+1):
        if(Num % i == 0):
            Fact = Fact + i
    return Fact


def main():
    A = int(input("Enter a Number: "))

    ret = AddFact(A)

    print("Addition of factors of given number is: ",ret)




if __name__ == "__main__":
    main()