class CircularLinkedList:
    def __init__(self):
        self.head = None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":
    cll = CircularLinkedList()

    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n4 = Node(40)

    cll.head = n1
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n1

    print(cll.head.data, cll.head.next.data, cll.head.next.next.data,
          cll.head.next.next.next.data, cll.head.next.next.next.next.data)
