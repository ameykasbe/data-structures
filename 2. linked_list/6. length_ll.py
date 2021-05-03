# https://www.geeksforgeeks.org/find-length-of-a-linked-list-iterative-and-recursive/

# A complete working Python program to find length of a
# Linked List iteratively

# Node
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

    # This function is in LinkedList class. It inserts
    # a new node at the beginning of Linked List.

    def push(self, new_data):

        # 1 & 2: Allocate the Node &
        #     Put in the data
        new_node = Node(new_data)

        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node

    # This function counts number of nodes in Linked List
    # iteratively, given 'node' as starting node.

    def get_count_iterative(self):
        count = 0
        ref = self.head
        while(ref):
            count += 1
            ref = ref.next
        return count


# Code execution starts here
if __name__ == '__main__':
    llist = LinkedList()
    llist.push(1)
    llist.push(3)
    llist.push(1)
    llist.push(2)
    llist.push(1)
    print("Count of nodes is :", llist.get_count_iterative())
