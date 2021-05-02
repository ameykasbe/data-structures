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


def find_span(price):
    stack = Stack(len(price))
    output = [1]
    stack.push(0)
    for i in range(1, len(price)):
        print("i=", i)
        while(not stack.is_empty() and price[stack.stack[stack.top]] <= price[i]):
            x = stack.pop()
            print("Popped element", x, "because",
                  price[stack.top], "<=", price[i])
        if stack.is_empty():
            print(f"Stack empty. Appending {i+1} to output.")
            output.append(i+1)
            print("Output = ", output)
        else:
            print(
                f"Stack is not empty. Stack = {stack.stack}.Appending {i-stack.peek()} to output.")
            output.append(i-stack.peek())
            print("Output = ", output)

        print(f"Pushing {i}.")
        stack.push(i)
        print("Stack = ", stack.stack)

    return output


if __name__ == "__main__":
    price = [10, 4, 5, 90, 120, 80]
    print(find_span(price))
