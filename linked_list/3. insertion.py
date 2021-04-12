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

    def insert_after_node(self, new_data, prev_node):
        if prev_node == None:
            print("The given previous node must be in a linked list.")
            return

        nn = Node(new_data)
        nn.next = prev_node.next
        prev_node.next = nn

    def insert_after_data(self, new_data, prev_data):
        prev_node = self.head
        while(prev_node):
            if prev_node.data != prev_data:
                prev_node = prev_node.next
            else:
                self.insert_after_node(new_data, prev_node)
                return
        print("Data not found")

    def append(self, new_data):
        nn = Node(new_data)
        if self.head == None:
            self.head = nn
            return

        last_node = self.head
        while(last_node.next):
            last_node = last_node.next
        last_node.next = nn


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == '__main__':
    # Creating linked list with head object referencing None
    ll = LinkedList()

    # Append
    ll.append(10)
    ll.append(20)
    ll.append(30)

    # Push
    ll.push(5)

    # Insert after node
    n20 = ll.head.next.next
    ll.insert_after_node(25, n20)

    # Insert after data
    ll.insert_after_data(27, 25)

    # Append
    ll.append(35)

    # Print List
    ll.print_list()
