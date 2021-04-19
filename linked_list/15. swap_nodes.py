# https://www.geeksforgeeks.org/swap-nodes-in-a-linked-list-without-swapping-data/

# Python program to swap two given nodes of a linked list

class LinkedList(object):
    def __init__(self):
        self.head = None

    # head of list
    class Node(object):
        def __init__(self, d):
            self.data = d
            self.next = None

    # Function to swap Nodes x and y in linked list by
    # changing links
    def swapNodes(self, x, y):
        if self.head == None:
            print("Linked list empty.")
            return

        n1 = None
        n2 = None
        ref = self.head

        while(ref.next):
            if ref.next.data == x:
                pn1 = ref
                n1 = ref.next
            if ref.next.data == y:
                pn2 = ref
                n2 = ref.next
            ref = ref.next

        # If one value lies in head
        if x == self.head.data or y == self.head.data:
            if y == self.head.data:
                pn2 = pn1
                n2 = n1
            n1 = self.head
            self.head = n2
        else:
            pn1.next = n2

        # If any missing
        if not (n1 and n2):
            print("One or more data not found.")
            return

        pn2.next = n1
        temp = n1.next
        n1.next = n2.next
        n2.next = temp
        return

    # Function to add Node at beginning of list.

    def push(self, new_data):

        # 1. alloc the Node and put the data
        new_Node = self.Node(new_data)

        # 2. Make next of new Node as head
        new_Node.next = self.head

        # 3. Move the head to point to new Node
        self.head = new_Node

    # This function prints contents of linked list starting
    # from the given Node
    def printList(self):
        tNode = self.head
        while tNode != None:
            print(tNode.data)
            tNode = tNode.next


# Driver program to test above function
llist = LinkedList()

# The constructed linked list is:
# 1->2->3->4->5->6->7
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
print("Linked list before calling swapNodes() ")
llist.printList()
llist.swapNodes(4, 1)
print("\nLinked list after calling swapNodes() ")
llist.printList()
