# Python3 program to remove duplicate
# nodes from a sorted linked list

# Node class
class Node:

    # Constructor to initialize
    # the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node
    # at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the
    # linked LinkedList

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next

    def delete_node(self, prev_node):
        del_node = prev_node.next
        prev_node.next = del_node.next
        del_node = None

    def duplicate_remove(self):
        if self.head == None:
            print("Linked List empty.")
            return
        ref = self.head
        while(ref.next):
            nxt = ref.next
            if nxt.data == ref.data:
                self.delete_node(ref)
                nxt = ref.next
            else:
                ref = ref.next

            # Driver Code
llist = LinkedList()

llist.push(20)
llist.push(13)
llist.push(13)
llist.push(11)
llist.push(11)
llist.push(11)
print("Created Linked List: ")
llist.printList()
print("Linked List after removing",
      "duplicate elements:")
llist.duplicate_remove()
llist.printList()
