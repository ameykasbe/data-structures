## http://geeksquiz.com/linked-list-set-1-introduction/

class LinkedList:
    def __init__(self):
        self.head = None


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

    print(ll.head.data, ll.head.next.data, ll.head.next.next.data)
