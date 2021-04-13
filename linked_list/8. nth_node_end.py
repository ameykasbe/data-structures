# https://www.geeksforgeeks.org/nth-node-from-the-end-of-a-linked-list/

# Python program to find n'th node from end using slow
# and fast pointer

# Node class
class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def nth_from_last(self, n):
        ref = self.head
        node = self.head
        if n < 1:
            print("n should be integer and greater than 0")
            return

        if ref == None:
            print("List is empty")
            return

        for i in range(n):
            if ref == None:
                print("n is greater than length of linked list.")
                return
            ref = ref.next

        while(ref):
            ref = ref.next
            node = node.next
        return node.data


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(35)

print(llist.nth_from_last(2))
