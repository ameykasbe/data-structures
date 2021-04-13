# https://www.geeksforgeeks.org//linked-list-set-3-deleting-node/
# https://www.geeksforgeeks.org/delete-a-linked-list-node-at-a-given-position/

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        ref = self.head
        while(ref):
            print(ref.data)
            ref = ref.next

    def push(self, new_data):
        nn = Node(new_data)
        nn.next = self.head
        self.head = nn

    def delete_node(self, key):
        prev_node = self.head

        # List is empty
        if prev_node == None:
            print("Linked list is empty.")
            return

        # If head node consists of key
        if prev_node.data == key:
            self.head = prev_node.next
            prev_node = None
            return

        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        ref = prev_node.next
        while(ref):
            if ref.data == key:
                break
            ref = ref.next
            prev_node = prev_node.next

        # If ref becomes None
        if ref == None:
            print("Key not found.")
            return

        # Unlink node
        prev_node.next = ref.next
        ref = None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == '__main__':
    # Creating linked list with head object referencing None
    ll = LinkedList()

    ll.push(10)
    ll.push(20)
    ll.push(30)
    ll.push(40)

    # Delete
    ll.delete_node(50)

    # Print List
    ll.print_list()
