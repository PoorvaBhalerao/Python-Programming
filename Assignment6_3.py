# Design python application which creates two threads as evenlist and oddlist. Both the 
# threads accept list of integers as parameter. Evenlist thread add all even elements 
#from input list and display the addition. Oddlist thread add all odd elements from input 
#list and display the addition

import threading

def EvenList(Received_List):   
    iSum = 0
    i = 0
    for i in range(len(Received_List)):
        if((Received_List[i]%2) == 0):
            iSum = iSum +Received_List[i]
    print("Even numbers Addition is: ",iSum)


def OddList(Received_List):   
    iSum = 0
    i = 0
    for i in range(len(Received_List)):
        if(Received_List[i]%2 != 0):
            iSum = iSum +Received_List[i]
    print("Odd numbers Addition is: ",iSum)
  

def main():
    iValue = int(input("Enter number of elements: "))

    Arr = list()

    print("Entered elements are: ")
    for num in range(iValue):
        num = int(input())
        Arr.append(num)

    #print(Arr)
    t1 = threading.Thread(target=EvenList,args=[Arr])
    t2 = threading.Thread(target=OddList,args=[Arr])

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()