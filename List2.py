# Arr = [11, 78.90, True, "Marvellous", 11]

# for no in Arr:
#     print(no)

# print("_____________________________________")

# for no in range(len(Arr)):
#     print(Arr[no])

# print("_____________________________________")

## Accept the number of elements from user and display list
def main():
    Size =int(input("Enter the number elements for list:"))
    Arr = list()
    
    print("Enter elements:")
    for i in range(Size):
        no = int(input())
        Arr.append(no)

    print("Entered elements are: ",Arr)
        

    
if __name__ == "__main__":
    main()


