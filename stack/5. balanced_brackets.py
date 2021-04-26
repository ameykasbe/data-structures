# https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/

class Stack:
    def __init__(self, max_size):
        self.stack = list()
        self.max_size = max_size
        self.top = -1

    def push(self, data):
        if self.top >= self.max_size:
            print("Stack overflow.")
            exit(1)
        self.top += 1
        self.stack.append(data)

    def pop(self):
        if self.top <= -1:
            print("Stack underflow.")
            exit(1)
        temp = self.stack.pop()
        self.top -= 1
        return temp

    def is_empty(self):
        if self.top == -1:
            return True
        return False

    def print_stack(self):
        if self.is_empty():
            print("Stack empty")
            return
        ref = self.top
        print("Printing stack.")
        while(ref >= 0):
            print(self.stack[ref])
            ref -= 1


def is_balanced(brackets):
    s = Stack(len(brackets))
    for i in brackets:
        if i in ['{', '(', '[']:
            s.push(i)
            print(f"Pushing '{i}'", s.stack)
        else:
            if s.is_empty():
                print("Empty", s.stack)
                return False
            x = s.pop()
            print(f"Popped '{x}'. {x} & {i}")
            if not ((i == "}" and x == "{") or (i == ")" and x == "(") or (i == "]" and x == "[")):
                print("Didn't match")
                return False
    print("Final", s.stack)
    if not s.is_empty():
        return False
    return True


if __name__ == "__main__":
    brackets = r'[()]{}{[()()]()}'
    print(is_balanced(brackets))
