# https://www.geeksforgeeks.org//search-an-element-in-a-linked-list-iterative-and-recursive/

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null

# Linked List class


class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head as None

    # This function insert a new node at the
    # beginning of the linked list
    def push(self, new_data):

        # Create a new Node
        new_node = Node(new_data)

        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node

    # This Function checks whether the value
    # x present in the linked list
    def search(self, x):
        ref = self.head
        while(ref):
            if ref.data == x:
                return True
            ref = ref.next
        return False


        # Code execution starts here
if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList()

    llist.push(10)
    llist.push(30)
    llist.push(11)
    llist.push(21)
    llist.push(14)

    print(llist.search(87))
