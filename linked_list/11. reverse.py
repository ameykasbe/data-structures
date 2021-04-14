# https://www.geeksforgeeks.org/reverse-a-linked-list/
# Python program to reverse a linked list
# Time Complexity : O(n)
# Space Complexity : O(1)

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

    def reverse(self):
        if self.head == None:
            print("Linked List empty.")
            return
        prev = None
        current = self.head
        while(current is not None):  # Note
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        self.head = prev

    # Function to insert a new node at the beginning

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data),
            temp = temp.next


# Driver code
llist = LinkedList()
llist.push(20)
llist.push(10)
llist.push(30)


print("Given Linked List")
llist.printList()
llist.reverse()
print("\nReversed Linked List")
llist.printList()
