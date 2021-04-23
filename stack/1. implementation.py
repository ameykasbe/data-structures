# # Using only fundamentals

class Stack:
    def __init__(self):
        self.stack = list()
        self.top = -1
        self.max_size = 5

    def push(self, data):
        if self.top >= self.max_size - 1:
            print(f"Stack overflow while pushing element {data}.")
            return
        self.stack.append(data)
        self.top += 1

    def pop(self):
        if self.top <= -1:
            print("Stack underflow.")
            return
        item = self.stack.pop()
        self.top -= 1
        return item

    def size(self):
        return (self.top + 1)

    def print_stack(self):
        if self.top <= -1:
            print("Stack empty")
            return
        ref = self.top
        print("Printing stack.")
        while(ref >= 0):
            print(self.stack[ref])
            ref -= 1

    def peek(self):
        if self.top <= -1:
            print("Stack empty")
            return
        return self.stack[self.top]


if __name__ == "__main__":
    s = Stack()

    s.push(5)
    s.push(4)
    s.push(3)
    s.push(2)
    s.push(1)
    s.push(100)

    s.print_stack()

    print("Peeking:", s.peek())

    print("Popping element:", s.pop())
    print("Popping element:", s.pop())
    print("Popping element:", s.pop())

    s.print_stack()
    print("Size of stack:", s.size())
    print("Popping element:", s.pop())
    print("Popping element:", s.pop())
    s.print_stack()
    print("Popping element:", s.pop())
