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
            return
        print("Forward traversal:")
        while(ref):
            print(ref.data)
            if ref.next == None:
                last = ref
            ref = ref.next

        print("Reverse traversal:")

        while(last.next):
            last = last.next
        while(last):
            print(last.data)
            last = last.prev

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

    def insert_after(self, key, data):
        nn = Node(data)
        ref = self.head
        if ref == None:
            print("LL Empty")
            return

        while(ref):
            if ref.data == key:
                break
            ref = ref.next
        if ref.next == None:
            ref.next = nn
            nn.prev = ref
            return
        if ref:
            nn.next = ref.next
            nn.prev = ref
            ref.next.prev = nn
            ref.next = nn
            return
        print("Key not found!")
        return


dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)

dll.insert_after(50, 55)

dll.print_list()
