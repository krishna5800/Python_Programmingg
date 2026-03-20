class Node:
    def __init__(self, Value):
        self.data = Value
        self.next = None

class SinglyLL:

    def __init__(self):
        self.first = None
        self.iCount = 0

    def InsertFirst(self, No):
        newn = Node(No)
        
        if self.first is None:
            self.first = newn
        else:
            newn.next = self.first
            self.first = newn

        self.iCount = self.iCount + 1

    def InsertLast(self, No):

        newn = Node(No)
        temp = self.first

        if self.first == None:
            self.first = newn
        else:
            while temp.next != None:
                temp = temp.next
        
            temp.next = newn
        
        self.iCount = self.iCount + 1

    def InsertAtPos(self, No, Pos):

        if(Pos < 1 or Pos > self.iCount+1):
            print("Invalid Position")
            return
         
        if Pos == 1:
            self.InsertFirst(No)
        elif Pos == self.iCount + 1:
            self.InsertLast(No)
        else:
            temp = self.first

            newn = Node(No)

            for i in range(1, Pos-1):
                temp = temp.next

            newn.next = temp.next
            temp.next = newn

            self.iCount = self.iCount + 1

    def DeleteFirst(self):

        if self.first == None:
            return
        elif self.first.next == None:
            self.first = None
        else:
            temp = self.first
            self.first = self.first.next

            temp.next = None

        self.iCount = self.iCount - 1

    def DeleteLast(self):
        temp = self.first

        if self.first == None:
            return
        elif self.first.next == None:
            self.first = None
        else:
            while temp.next.next != None:
                temp = temp.next
        
            temp.next = None

        self.iCount = self.iCount - 1
    
    def DeleteAtPos(self, Pos):

        if(Pos < 1 or Pos > self.iCount):
            print("Invalid Position")
            return
         
        if Pos == 1:
            self.DeleteFirst()
            return
        
        elif Pos == self.iCount:
            self.DeleteLast()
            return
        
        else:
            temp = self.first

            for i in range(1, Pos-1):
                temp = temp.next

            temp.next = temp.next.next

            self.iCount = self.iCount - 1

    def Display(self):
        temp = self.first

        while temp is not None:
            print("| ", temp.data ," |->", end = " ")
            temp = temp.next
        print(None)

    def Count(self):
        return self.iCount

def main():
    sobj = SinglyLL()
    Ret = 0

    sobj.InsertFirst(51)
    sobj.InsertFirst(21)
    sobj.InsertFirst(11)

    sobj.Display()
    Ret = sobj.Count()
    print("Count is : ", Ret)

    sobj.InsertLast(101)
    sobj.InsertLast(111)
    sobj.InsertLast(121)

    sobj.Display()
    Ret = sobj.Count()
    print("Count is : ", Ret)

    sobj.DeleteFirst()

    sobj.Display()
    Ret = sobj.Count()
    print("Count is : ", Ret)

    sobj.DeleteLast()

    sobj.Display()
    Ret = sobj.Count()
    print("Count is : ", Ret)

    sobj.InsertAtPos(105, 4)

    sobj.Display()
    Ret = sobj.Count()
    print("Count is : ", Ret)

    sobj.DeleteAtPos(4)

    sobj.Display()
    Ret = sobj.Count()
    print("Count is : ", Ret)

if __name__ == "__main__":
    main()