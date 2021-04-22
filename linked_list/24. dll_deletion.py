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

    def delete(self, key):
        ref = self.head
        if ref == None:
            print("List empty.")
            return

        if ref.data == key:
            self.head = ref.next
            if ref.next:
                ref.next.prev = None
            ref = None
            return

        while(ref):
            if ref.data == key:
                break
            ref = ref.next

        if ref:
            if ref.next == None:
                ref.prev.next = None
                ref = None
                return
            ref.next.prev = ref.prev
            ref.prev.next = ref.next
            ref = None
            return
        print("Key not found")
        return


dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)
dll.append(50)

dll.delete(10)
# dll.delete(20)
# dll.delete(50)
# dll.delete(60)

dll.print_list()
