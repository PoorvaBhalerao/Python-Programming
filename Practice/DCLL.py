# Doubly Circular Linked List

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyCL:
    
    def __init__(self):
        print("Object of DoublyCL is created")
        self.first = None
        self.last = None
        self.iCount = 0

    def InsertFirst(self, no):
        
        newn = node(no)

        if(self.first == None and self.last == None):
            self.first = newn
            self.last = newn
        else:
            newn.next = self.first
            self.first.prev = newn
            self.first = newn

        self.last.next = self.first
        self.first.prev = self.last
        self.iCount += 1


    def InsertLast(self, no):

        newn = node(no)

        if(self.first == None and self.last == None):
            self.first = newn
            self.last = newn
        else:
            self.last.next = newn
            newn.prev = self.last
            self.last = newn

        self.last.next = self.first
        self.first.prev = self.last
        self.iCount += 1


    def Display(self):
        temp = self.first

        print("<=> ",end = "")
        bFlag = True
        while bFlag:
            print(temp.data, end=" <=> ")
            temp = temp.next
            if(temp == self.last.next):
                bFlag = False
        print()

        
    def Count(self):
        return self.iCount
    
    def DeleteFirst(self):

        if(self.first == None and self.last == None):
            print("LL is empty")
            return
        elif(self.first == self.last):
            self.first = None
            self.last = None
        else:
            self.first = self.first.next

        self.last.next = self.first
        self.first.prev = self.last            
        self.iCount -= 1 


    def DeleteLast(self):

        if(self.first == None and self.last == None):
            print("LL is empty")
            return
        elif(self.first == self.last):
            self.first = None
            self.last = None
        else:
            self.last = self.last.prev

        self.last.next = self.first
        self.first.prev = self.last            
        self.iCount -= 1 

    
    def InsertAtPos(self, no, pos):
        
        if((pos < 1) | (pos > self.iCount+1)):
            print("LL is empty")
            return
        
        if(pos == 1):
            self.InsertFirst(no)
        elif(pos == self.iCount+1):
            self.InsertLast(no)
        else:
            newn = node(no)
            temp = self.first

            for iCnt in range(1, pos-1):
                temp = temp.next
                iCnt += 1
            newn.next = temp.next
            temp.next.prev = newn
            newn.prev = temp
            temp.next = newn

            self.iCount += 1


    def DeleteAtPos(self, pos):
        if((pos < 1) | (pos > self.iCount+1)):
            print("LL is empty")
            return
        
        if(pos == 1):
            self.InsertFirst(no)
        elif(pos == self.iCount+1):
            self.InsertLast(no)
        else:
            temp = self.first

            for iCnt in range(1, pos-1):
                temp = temp.next
                iCnt += 1

            temp.next = temp.next.next
            temp.next.prev = temp            

            self.iCount -= 1



def main():
    obj = DoublyCL()
    iRet = 0

    obj.InsertFirst(51)
    obj.InsertFirst(21)
    obj.InsertFirst(11)

    obj.Display()
    iRet = obj.Count()
    print("Number of nodes are: ",iRet)

    obj.InsertLast(101)
    obj.InsertLast(111)
    obj.InsertLast(121)

    obj.Display()
    iRet = obj.Count()
    print("Number of nodes are: ",iRet)

    obj.DeleteFirst()

    obj.Display()
    iRet = obj.Count()
    print("Number of nodes are: ",iRet)

    obj.DeleteLast()

    obj.Display()
    iRet = obj.Count()
    print("Number of nodes are: ",iRet)

    obj.InsertAtPos(555,4)

    obj.Display()
    iRet = obj.Count()
    print("Number of nodes are: ",iRet)

    obj.DeleteAtPos(4)

    obj.Display()
    iRet = obj.Count()
    print("Number of nodes are: ",iRet)




if __name__ == "__main__":
    main()