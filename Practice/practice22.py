# Write a program which accept number from user and check whether it contains zero or not
#Input: 2395
#Output: There is not zero
#Input: 2509
#Output: It contains zero

class Display():

    def __init__(self, iNo):
        self.iNo = iNo

    def DisplayZero(self):
        self.bFlag = False
        while(self.iNo != 0):
            iDigit = self.iNo % 10
            if(iDigit == 0):
                self.bFlag = True
                break
            self.iNo = self.iNo / 10
        
        if(self.bFlag == True):
            print("It contains Zero")
        else:
            print("There is no Zero")


def main():

    iValue = int(input("Enter a number: "))

    obj = Display(iValue)
    obj.DisplayZero()


if __name__ == "__main__":
    main()
        