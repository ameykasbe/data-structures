# https://www.geeksforgeeks.org/remove-duplicates-from-an-unsorted-linked-list/

# Python3 program to remove duplicates
# from unsorted linkedlist
class Node:

    def __init__(self, data):

        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):

        self.head = None

    # Function to print nodes in a
    # given linked list
    def printlist(self):

        temp = self.head

        while (temp):
            print(temp.data, end=" ")
            temp = temp.next

    def delete_node_to_prev(self, prev_node):
        dn = prev_node.next
        prev_node.next = dn.next
        dn = None

    def remove_duplicates(self):
        hash_table = set()
        ref = self.head

        if ref == None:
            print("Linked List empty.")
            return

        hash_table.add(ref.data)
        while(ref.next):
            nxt = ref.next
            if nxt.data in hash_table:
                self.delete_node_to_prev(ref)
            else:
                hash_table.add(nxt.data)
                ref = ref.next


if __name__ == "__main__":

    # Creating Empty list
    llist = LinkedList()
    llist.head = Node(10)
    second = Node(12)
    third = Node(11)
    fourth = Node(11)
    fifth = Node(12)
    sixth = Node(11)
    seventh = Node(10)

    # Connecting second and third
    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seventh

    # Printing data
    print("Linked List before removing Duplicates.")
    llist.printlist()
    llist.remove_duplicates()
    print("\nLinked List after removing duplicates.")
    llist.printlist()
