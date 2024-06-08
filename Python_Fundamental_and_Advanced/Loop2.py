def Display(No):
    i = 0
    if(No<=0):
        print("Invalid input")
        return
    
    # for i in range(0,No):
    #     print("Jay Ganesh...", end = " ")   #if want to print on same line then use end = " "

    while(i < No):
        print("Jay Ganesh...", end = " ")
        i = i +1


def main():
    Cnt = int(input("Enter Frequency:   "))

    Display(Cnt)

if __name__ == "__main__":
    main()

