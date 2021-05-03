# # Using only fundamentals

class Stack:
    def __init__(self, max_size):
        self.stack = list()
        self.top = -1
        self.max_size = max_size

    def is_empty(self):
        if self.top <= -1:
            return True
        return False

    def push(self, data):
        if self.top >= self.max_size - 1:
            print(f"Stack overflow while pushing element {data}.")
            exit(1)
        self.stack.append(data)
        self.top += 1

    def pop(self):
        if self.is_empty():
            print("Stack underflow.")
            exit(1)
        item = self.stack.pop()
        self.top -= 1
        return item

    def size(self):
        return (self.top + 1)

    def print_stack(self):
        if self.is_empty():
            print("Stack empty")
            return
        ref = self.top
        print("Printing stack.")
        while(ref >= 0):
            print(self.stack[ref])
            ref -= 1

    def peek(self):
        if self.is_empty():
            print("Stack empty")
            return
        return self.stack[self.top]


if __name__ == "__main__":
    s = Stack(5)

    # Push
    s.push(5)
    s.push(4)
    s.push(3)
    s.push(2)
    s.push(1)

    # Stack overflow
    # s.push(100)

    # Print stack
    s.print_stack()

    # Peak
    print("Peeking:", s.peek())

    # Pop
    print("Popping element:", s.pop())
    print("Popping element:", s.pop())
    print("Popping element:", s.pop())

    # Size
    print("Size of stack:", s.size())

    # Check empty print
    print("Popping element:", s.pop())
    print("Popping element:", s.pop())
    s.print_stack()
    # Underflow
    # x = s.pop()
