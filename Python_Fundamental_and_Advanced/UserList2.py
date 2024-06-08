# Accept number of elements from user and display it and display Addition is elements in List

def Addition(Data):
    Sum = 0
    for no in Data:
        Sum = Sum + no
    return Sum


def main():
    print("Enter number of elements you want to insert in list:")
    size = int(input())

    Arr = list()

    print("Enter elemenmts:")
    for i in range(size):
        no = int(input())
        Arr.append(no)

    print("Entered elements are:", Arr)

    Result = Addition(Arr)
    print("Summation of all elements are: ", Result)


if __name__ == "__main__":
    main()