class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        ref = self.head
        if ref == None:
            print("DLL empty.")
        while(ref):
            print(ref.data)
            ref = ref.next

    def push(self, new_data):
        nn = Node(new_data)
        if self.head == None:
            self.head = nn
            return
        nn.next = self.head
        self.head.prev = nn
        self.head = nn

    def append(self, new_data):
        nn = Node(new_data)
        ref = self.head
        if ref == None:
            self.head = nn
            return
        while(ref.next):
            ref = ref.next
        nn.prev = ref
        ref.next = nn


dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)

dll.print_list()
