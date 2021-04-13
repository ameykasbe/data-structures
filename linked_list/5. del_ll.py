# Iterate through the linked list and delete all the nodes one by one. The main point here is not to access the next of the current pointer if the current pointer is deleted.

class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # push function to add node in front of llist
    def push(self, new_data):

        # Allocate the Node &
        # Put in the data
        new_node = Node(new_data)

        # Make next of new Node as head
        new_node.next = self.head

        # Move the head to point to new Node
        self.head = new_node

    def delete_list(self):
        # In Java and Python, automatic garbage collection happens, so deleting a linked list is easy. Just need to change head to null.
        self.head = None

        # OR
        current = self.head
        while(current):
            prev = current
            current = current.next
            print("Deleting {}".format(prev.data))
            prev = None
        print("Linked List deleted successfully.")


if __name__ == '__main__':
    llist = LinkedList()

    llist.push(1)
    llist.push(2)
    llist.push(3)
    llist.push(4)

    llist.delete_list()
