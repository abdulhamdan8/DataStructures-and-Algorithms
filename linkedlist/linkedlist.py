# create node
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


# linked list
class Linkedlist:
    def __init__(self):
        self.head = None

    # traversal
    def print_linkedlist(self):
        # check LL is empty
        if self.head is None:
            print("LL is empty")
        n = self.head
        while n is not None:
            print(n.data,"-->",end=" ")
            n = n.ref
        print('\n')
    def addbegin(self,data):
        new_node = Node(data)  # creates new node and stores location in new_node
        new_node.ref = self.head #assigning head to newly created node
        self.head = new_node #current head is new node

    def addend(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref = new_node
    def add_after(self,data,x):
        n=self.head
        while n.ref is not None:
            if n.ref == x:
                break
            n=n.ref
        if n is None:
            print("not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref =new_node
    def add_before(self,data,x):
        if self.head is None:
            print("LL is empty")
        if self.head.data == x:
            new_node =Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def delete_begin(self):
        if self.head is None:
            print("LL is empty")
        else:
            self.head = self.head.ref
    def delete_last(self):
        if self.head is None:
            print("LL is empty")
        else:
            n= self.head
            while n.ref is not None:
                if n.ref.ref is None:
                    n.ref = None
                    break
                n=n.ref

    def delete_by_value(self,data):
        if self.head is None:
            print("ll is empty")
            return
        if data == self.head.data:
            self.head = self.head.ref
            return
        n=self.head
        while n.ref is not None:
            if n.ref.data == data:
                break
            n = n.ref
        if n.ref is None:
            print("node not found")
        else:
            n.ref = n.ref.ref




#5-3-20-44-10


LL1 = Linkedlist()
LL1.addbegin(3)
LL1.addend(20)
LL1.add_after(10,20)
LL1.addbegin(5)
LL1.add_before(44,3)
LL1.print_linkedlist()
LL1.delete_begin()
LL1.print_linkedlist()
# LL1.delete_last()
LL1.delete_by_value(44)
LL1.print_linkedlist()
