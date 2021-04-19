# https://leetcode.com/problems/swap-nodes-in-pairs/discuss/171788/Python-or-Dummynode

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        nn = Node(new_data)
        nn.next = self.head
        self.head = nn

    def print_list(self):
        ref = self.head
        while(ref):
            print(ref.data)
            ref = ref.next

    def swap_adj(self):
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        current = self.head
        while(current and current.next):
            nxt = current.next
            prev.next = nxt
            current.next = nxt.next
            nxt.next = current
            prev = current
            current = current.next
        self.head = dummy.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Driver code
llist = LinkedList()
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

llist.print_list()

llist.swap_adj()

llist.print_list()
