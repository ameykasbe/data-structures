class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        ref = self.head
        while(ref):
            print(ref.data)
            ref = ref.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == '__main__':
    # Creating linked list with head object referencing None
    ll = LinkedList()

    # Creating nodes
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)

    # Link three nodes
    ll.head = n1
    n1.next = n2
    n2.next = n3

    ll.print_list()
