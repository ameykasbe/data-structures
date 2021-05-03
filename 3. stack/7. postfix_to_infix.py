class Conversion:
    def __init__(self, max_size):
        self.stack = list()
        self.top = -1
        self.max_size = max_size
        self.precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2
        }

    def is_operand(self, ch):
        return ch.isalpha()

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

    def is_greater(self, i):
        try:
            if self.precedence[i] > self.precedence[self.peek()]:
                return True
            return False
        except KeyError:
            return False

    def convert(self, exp):
        for i in exp:
            if self.is_operand(i):
                self.push(i)
            else:
                y = self.pop()
                x = self.pop()
                string = f"({x}{i}{y})"
                self.push(string)
        if self.top == 0:
            return self.pop()
        print("The user input has too many values")
        exit(1)


if __name__ == "__main__":
    exp = "xab+cd*-*y/"
    itop = Conversion(len(exp))
    infix = itop.convert(exp)
    print(infix)
