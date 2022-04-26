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
            print(n.data)
            n = n.ref
    def addbegin(self,data):
        new_node = Node(data)  # creates new node and stores location in new_node
        new_node.ref = self.head #assigning head to newly created node
        self.head = new_node #current head is new node


LL1 = Linkedlist()
LL1.addbegin(3)
LL1.addbegin(5)

LL1.print_linkedlist()
