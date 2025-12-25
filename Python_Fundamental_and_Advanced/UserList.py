
def main():
    print("Enter number of elements you want to insert in list:")
    size = int(input())

    Arr = list()

    print("Enter elemenmts:")

    for i in range(size):
        no = int(input())
        Arr.append(no)

    print("Entered elemets are:", Arr)

if __name__ == "__main__":
    main()

