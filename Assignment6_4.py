# Design python application which creates three threads as small, capital, digits. All the 
# threads accepts string as parameter. Small thread display number of small characters, 
# capital thread display number of capital characters and digits thread display number of 
# digits. Display id and name of each thread.
import threading
import os

def Smallchar(Lst):
    print("PID of small process:",os.getpid())
    #print("TID of small thread ",threading.get_ident())
    print("Name of thread:",threading.current_thread())
    char = '\0'
    i = 0
    iCnt = 0
    for char in Lst:
        if(char.islower()):
            iCnt = iCnt + 1
            #print("small:"+Lst[i])
        i = i+1
    print("No of small letters:",iCnt)


def Capitalchar(Lst):
    print("PID of capital process:",os.getpid())
    #print("TID of capital thread ",threading.get_ident())
    print("Name of thread:",threading.current_thread())
    char = '\0'
    i = 0
    iCnt = 0
    for char in Lst:
        if(char.isupper()):
            iCnt = iCnt+1
            #print("capital:"+Lst[i])
        i = i+1
    print("No of capital letters:",iCnt)


def Digits(Lst):
    print("PID of digits process:",os.getpid())
    #print("TID of digits thread ",threading.get_ident())
    print("Name of thread:",threading.current_thread())
    char = '\0'
    #i = 0
    iCnt = 0
    for char in Lst:
        if(char.isdigit()):
            iCnt = iCnt + 1
    print("Count of digits is:",iCnt)


def main():
    Str = input("Pls enter a word that contains capital and small letters as well as numbers:")

    Str_lst = list(Str)
    #print(Str_lst)

    small = threading.Thread(target=Smallchar,args=[Str_lst])
    capital = threading.Thread(target=Capitalchar,args=[Str_lst])
    digits = threading.Thread(target=Digits,args=[Str_lst])

    small.start()
    capital.start()
    digits.start()
   
    
    small.join()
    capital.join()
    digits.join()
    
    



if __name__ == "__main__":
    main()