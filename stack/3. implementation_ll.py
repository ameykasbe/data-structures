class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.last = None

    def is_empty(self):
        if self.last == None:
            return True
        return False

    def push(self, data):
        nn = StackNode(data)
        nn.next = self.last
        self.last = nn

    def pop(self):
        if self.is_empty():
            return -1
        temp = self.last
        data = temp.data
        self.last = self.last.next
        temp = None
        return data

    def peek(self):
        if self.is_empty():
            return -1
        return self.last.data

    def print_stack(self):
        if self.is_empty():
            print("Stack empty")
            return
        ref = self.last
        print("Printing stack.")
        while(ref):
            print(ref.data)
            ref = ref.next

    def size(self):
        count = 0
        ref = self.last
        while(ref):
            count += 1
            ref = ref.next
        return count


if __name__ == "__main__":
    s = Stack()

    s.push(5)
    s.push(4)
    s.push(3)
    s.push(2)
    s.push(1)

    s.print_stack()

    print("Peeking:", s.peek())

    pop_ = s.pop()
    if pop_ == -1:
        print("Stack empty.")
    else:
        print("Popping element:", pop_)

    pop_ = s.pop()
    if pop_ == -1:
        print("Stack empty.")
    else:
        print("Popping element:", pop_)

    pop_ = s.pop()
    if pop_ == -1:
        print("Stack empty.")
    else:
        print("Popping element:", pop_)

    s.print_stack()
    print("Size of stack:", s.size())
    pop_ = s.pop()
    if pop_ == -1:
        print("Stack empty.")
    else:
        print("Popping element:", pop_)

    pop_ = s.pop()
    if pop_ == -1:
        print("Stack empty.")
    else:
        print("Popping element:", pop_)
    s.print_stack()
    pop_ = s.pop()
    if pop_ == -1:
        print("Stack empty.")
    else:
        print("Popping element:", pop_)
