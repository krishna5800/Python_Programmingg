# Done
class Node:
    def __init__(self, Value):
        self.data = Value
        self.next = None

class SinglyLL:

    # Done
    def __init__(self):
        self.first = None
        self.iCount = 0

    # Done
    def InsertFirst(self, No):
        newn = Node(No)
        
        if self.first is None:
            self.first = newn
        else:
            newn.next = self.first
            self.first = newn

        self.iCount = self.iCount + 1

    # Done
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
        pass

    def DeleteFirst(self):
        pass

    def DeleteLast(self):
        pass

    def DeleteAtPos(self, Pos):
        pass

    # Done
    def Display(self):
        temp = self.first

        while(temp != None):
            print("| ", temp.data ," |->", end = " ")
            temp = temp.next

        print("None")

    # Done
    def Count(self):
        return self.iCount

def main():
    sobj = SinglyLL()

    sobj.InsertFirst(101)
    sobj.InsertFirst(51)
    sobj.InsertFirst(21)
    sobj.InsertFirst(11)

    print("Elements of Linked List are : ")
    sobj.Display()
    
    print("Number of elements in Linked List are : ", sobj.Count())

    sobj.InsertLast(111)
    sobj.InsertLast(121)

    print("Elements of Linked List are : ")
    sobj.Display()
    
    print("Number of elements in Linked List are : ", sobj.Count())

if __name__ == "__main__":
    main()