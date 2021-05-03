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

    def push(self, data):
        nn = Node(data)
        if self.head == None:
            self.head = nn
            nn.next = nn
            return

        last = self.head.next
        while(last.next is not self.head):
            last = last.next

        nn.next = self.head
        last.next = nn
        self.head == nn

    def append(self, data):
        nn = Node(data)

        if self.head == None:
            self.head = nn
            nn.next = nn
            return

        last = self.head.next
        while(last.next is not self.head):
            last = last.next

        last.next = nn
        nn.next = self.head

    def insert_after(self, data, key):
        if self.head == None:
            print("Linked List empty.")

        nn = Node(data)

        prev = self.head
        if prev.data == key:
            nn.next = prev.next
            prev.next = nn
            return
        prev = prev.next

        while (prev is not self.head):
            if prev.data == key:
                nn.next = prev.next
                prev.next = nn
                return
            prev = prev.next
        print("Key not found.")

    def delete(self, key):
        if self.head == None:
            print("CLL Empty.")
            return

        if self.head.next == self.head:
            self.head = None
            return

        prev = self.head
        curr = self.head.next

        while(curr != self.head):
            if curr.data == key:
                prev.next = curr.next
                curr = None
                return
            prev = prev.next
            curr = curr.next
        if curr.data == key:
            self.head = curr.next
            prev.next = curr.next
            curr = None
            return
        print("Key not found.")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


if __name__ == "__main__":
    cll = CircularLinkedList()

    cll.append(10)
    cll.append(20)
    cll.append(30)
    cll.append(40)
    cll.append(50)
    cll.insert_after(55, 50)
    cll.delete(10)
    cll.print_list()
