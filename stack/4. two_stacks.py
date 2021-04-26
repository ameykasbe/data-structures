# # https://www.geeksforgeeks.org/implement-two-stacks-in-an-array/

class TwoStack:
    def __init__(self, max_size):
        self.stack = [None] * max_size
        self.max_size = max_size
        self.top1 = -1
        self.top2 = max_size

    def push1(self, data):
        if self.top1 + 1 >= self.top2:
            print("Stack overflow stack 1.")
            exit(1)
        self.top1 += 1
        self.stack[self.top1] = data

    def push2(self, data):
        if self.top2 - 1 <= self.top1:
            print("Stack overflow stack 2.")
            exit(1)
        self.top2 -= 1
        self.stack[self.top2] = data

    def pop1(self):
        if self.top1 <= -1:
            print("Stack underflow stack 1")
            exit(1)
        item = self.stack[self.top1]
        self.top1 -= 1
        return item

    def pop2(self):
        if self.top2 >= self.max_size:
            print("Stack underflow stack 2")
            exit(1)
        item = self.stack[self.top2]
        self.top2 += 1
        return item


if __name__ == "__main__":
    # Driver program to test twoStacks class
    ts = TwoStack(5)
    ts.push1(5)
    ts.push2(10)
    ts.push2(15)
    ts.push1(11)
    ts.push2(7)

    print("Popped element from stack1 is " + str(ts.pop1()))
    ts.push2(40)
    print("Popped element from stack2 is " + str(ts.pop2()))

    # Output
    # Popped element from stack1 is 11
    # Popped element from stack2 is 40
