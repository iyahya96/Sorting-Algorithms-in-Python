class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self,data):
        newnode = Node(data)


    def delete(self,data,index):
        pass

    def insert(self,data,index):
        newnode = Node(data)
        if index == 0:
            newnode.next = self.head
            self.head = newnode
        if index == :
            self.tail.next = newnode
            self.tail = newnode


linkedlist = LinkedList()
linkedlist.insert(5,0)
linkedlist.insert(4,1)
linkedlist.insert(3,2)
linkedlist.insert(2,3)