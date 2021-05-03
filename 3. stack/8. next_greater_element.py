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


def next_greater(arr):
    output = list()
    stack = Stack(len(arr))
    for i in arr[::-1]:
        while(not stack.is_empty() and stack.peek() < i):
            stack.pop()
        if stack.is_empty():
            output.append(-1)
        else:
            output.append(stack.peek())
        stack.push(i)
    return output[::-1]


if __name__ == "__main__":
    # arr = [4, 5, 2, 25]
    arr = [10, 4, 5, 90, 120, 80]
    print(next_greater(arr))
