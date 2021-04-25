class Stack:
    def __init__(self, max_size):
        self.top = -1
        self.max_size = max_size
        self.stack = [None] * max_size

    def push(self, data):
        if self.top >= self.max_size - 1:
            print(f"Stack overflow while pushing elemeng {data}.")
            exit(1)
        self.top += 1
        self.stack[self.top] = data

    def pop(self):
        if self.top <= -1:
            print("Stack underflow")
            return
        item = self.stack[self.top]
        self.top -= 1
        return item

    def size(self):
        return self.top + 1

    def print_stack(self):
        if self.top <= -1:
            print("Stack empty")
            return
        ref = self.top
        while(ref >= 0):
            print(self.stack[ref])
            ref -= 1

    def peek(self):
        if self.top <= -1:
            print("Stack empty.")
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
