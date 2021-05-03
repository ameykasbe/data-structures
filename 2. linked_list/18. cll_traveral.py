class CircularLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        ref = self.head

        if ref == None:
            print("Circular Linked List empty.")
            return

        print(ref.data)
        ref = ref.next

        while(ref is not self.head):
            print(ref.data)
            ref = ref.next


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

    cll.print_list()
