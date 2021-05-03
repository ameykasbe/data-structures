class Stack:
    def __init__(self, max_size):
        self.stack = list()
        self.top = -1
        self.max_size = max_size

    def push(self, data):
        if self.top >= self.max_size - 1:
            print("Stack overflow.")
            exit(1)

        self.top += 1
        self.stack.append(data)

    def pop(self):
        if self.top <= -1:
            print("Stack underflow.")
            exit(1)
        item = self.stack.pop()
        self.top -= 1
        return item

    def is_empty(self):
        if self.top <= -1:
            return True
        return False

    def peek(self):
        if self.top <= -1:
            print("Stack empty")
            exit(1)
        return self.stack[self.top]

    def insert_at_bottom(self, item):
        if self.is_empty():
            self.push(item)
        else:
            temp = self.pop()
            self.insert_at_bottom(item)
            self.push(temp)

    def reverse(self):
        if not self.is_empty():
            temp = stack.pop()
            self.reverse()
            self.insert_at_bottom(temp)
        # else: # Doesn't matter
        #     return


if __name__ == "__main__":
    stack = Stack(10)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.reverse()
    print(stack.stack)
