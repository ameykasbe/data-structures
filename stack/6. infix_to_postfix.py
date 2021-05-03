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
        postfix = list()
        for i in exp:
            if self.is_operand(i):
                postfix.append(i)
                print(f"Appended {i} to postfix")
            elif (self.is_empty()) or (self.peek() == '(') or (i == '(') or self.is_greater(i):
                self.push(i)
                print(f"Pushed {i} to stack.")
            elif i == ')':
                while(not self.is_empty() and self.peek() != '('):
                    x = self.pop()
                    postfix.append(x)
                    print(f"Appended {x} to postfix")
                if self.is_empty():
                    print("Unbalanced paranthesis.")
                    exit(1)
                self.pop()
            else:
                while((not self.is_empty()) and (self.peek() != '(') and (not self.is_greater(i))):
                    x = self.pop()
                    postfix.append(x)
                    print(f"Appended {x} to postfix")
                self.push(i)
                print(f"Pushed {i} to stack")
        while(not self.is_empty()):
            x = self.pop()
            postfix.append(x)
            print(f"Appended {x} to postfix")
        return ("".join(postfix))


if __name__ == "__main__":
    exp = "x*(a+b-c*d)/y"
    itop = Conversion(len(exp))
    postfix = itop.convert(exp)
    print(postfix)
