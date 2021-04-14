# https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Print the linked list
    def print_list(self):
        node = self.head
        while node:
            print(str(node.data) + "->", end="")
            node = node.next
        print("NULL")

    def print_middle(self):
        slow = self.head
        fast = self.head

        if slow == None:
            print("List empty")
            return

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        print(slow.data)


# Code execution starts here
if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList()

    for i in range(5, 1, -1):
        llist.push(i)
    llist.print_list()
    llist.print_middle()
