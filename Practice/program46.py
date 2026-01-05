# Accept number of elements from user and display elments

def Display(elements):

    print("Entered elements are: ")

    for no in elements:
        print(no)


def main():

    iValue = int(input("Enter number of elements you want to enter: "))

    listelements = []

    print("Enter elements: ")

    for n in range(iValue):
        no = int(input())
        listelements.append(no)

    Display(listelements)



if __name__ == "__main__":
    main()


