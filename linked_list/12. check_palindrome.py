# Python3 program to check if
# linked list is palindrome

# Node class
class Node:

    # Constructor to initialize
    # the node object
    def __init__(self, data):

        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):

        self.head = None

    # Function to insert a new node
    # at the beginning
    def push(self, new_data):

        # Allocate the Node &
        # Put in the data
        new_node = Node(new_data)

        # Link the old list off the new one
        new_node.next = self.head

        # Move the head to point to new Node
        self.head = new_node

    # A utility function to print
    # a given linked list
    def printList(self):

        temp = self.head

        while(temp):
            print(temp.data, end="->")
            temp = temp.next

        print("NULL")

    def find_middle_is_even(self):
        slow = self.head
        fast = self.head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        if fast == None:
            return slow, True
        return slow, False

    def reverse(self, node):
        prev = None
        current = node
        while(current is not None):
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        node = prev
        return node

    def is_palindrome(self):
        middle, even = self.find_middle_is_even()
        if not even:
            middle = middle.next
        middle = self.reverse(middle)
        start = self.head
        is_pal = True
        while(middle):
            if start.data != middle.data:
                is_pal = False
                break
            middle = middle.next
            start = start.next
        middle = self.reverse(middle)
        return is_pal


# Driver code
if __name__ == '__main__':

    l = LinkedList()
    s = ['a', 'b', 'a']  # True
    # s = ['a', 'b', 'b']  # False
    # s = ['a', 'b', 'b', 'a']  # True
    # s = ['a', 'b', 'a', 'a']  # False
    # s = ['a', 'b']  # False
    # s = ['a']  # True

    if (l.is_palindrome()):
        print("Is Palindrome\n")
    else:
        print("Not Palindrome\n")
