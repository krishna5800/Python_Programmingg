class Node:
    def __init__(self, Value):
        self.data = Value
        self.next = None

def main():
    head = None

    obj1 = Node(11)
    obj2 = Node(21)
    obj3 = Node(51)
    obj4 = Node(101)

    head = obj1
    obj1.next = obj2
    obj2.next = obj3
    obj3.next = obj4
    obj4.next = None

    temp = head

    # (temp != None)
    while temp is not None:
        print("| ", temp.data ," |->", end = " ")
        temp = temp.next

    print(None)

if __name__ == "__main__":
    main()