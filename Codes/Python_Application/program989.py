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

    def InsertFirst(self, No):
        newn = Node(No)
        
        if self.first is None:
            self.first = newn
        else:
            newn.next = self.first
            self.first = newn

        self.iCount = self.iCount + 1

    def InsertLast(self, No):
        pass

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

if __name__ == "__main__":
    main()