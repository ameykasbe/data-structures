# https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/
# Python program to detect loop in the linked list

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

    # Utility function to print it the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def detect_loop(self):
        slow = self.head
        fast = self.head

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# Driver program for testing
llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(10)

# Create a loop for testing
llist.head.next.next.next.next = llist.head

if llist.detect_loop():
    print("Loop found")
else:
    print("No loop")
    llist.printList()
