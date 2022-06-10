class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def contains(self, value):
        return value in self.stack

    def is_empty(self):
        return len(self.stack) == 0

    def __repr__(self) -> str:
        stack = self.stack.copy()
        stack.reverse()
        return 'top -> ' + str(stack)

    def __str__(self) -> str:
        return repr(self)
