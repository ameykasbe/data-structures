class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

dll = DoublyLinkedList

dll.head = n1
n1.next = n2

n2.prev = n1
n2.next = n3

n3.prev = n2
n3.next = n4

n4.prev = n1

print(dll.head.data)
print(dll.head.next.data, dll.head.next.prev.data)
print(dll.head.next.next.data, dll.head.next.next.prev.data)
print(dll.head.next.next.next.data, dll.head.next.next.next.prev.data)
