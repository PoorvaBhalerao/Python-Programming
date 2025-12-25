# Singly Circular Linked List

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyCL:
    
    def __init__(self):
        print("Object of SinglyCL is created")
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
            self.first = newn

        self.last.next = self.first
        self.iCount += 1


    def InsertLast(self, no):

        newn = node(no)

        if(self.first == None and self.last == None):
            self.first = newn
            self.last = newn
        else:
            temp = self.first
            while(temp.next != self.first):
                temp = temp.next
            temp.next = newn
            self.last = newn

        self.last.next = self.first
        self.iCount += 1


    def Display(self):
        temp = self.first

        if self.first is None:
            print("NULL")
            return

        bFlag = True
        print("-> ",end = "")
        while bFlag:
            print(temp.data, end=" -> ")
            temp = temp.next    
            if (temp == self.last.next):
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
        self.iCount -= 1


    def DeleteLast(self):

        if(self.first == None and self.last == None):
            print("LL is empty")
            return
        elif(self.first == self.last):
            self.first = None
            self.last = None
        else:
            temp = self.first
            while(temp.next != self.last):
                temp = temp.next

            temp.next = None
            self.last = temp

        self.last.next = self.first            
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

            self.iCount -= 1



def main():
    obj = SinglyCL()
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