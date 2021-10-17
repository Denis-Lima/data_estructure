class Stack():
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, value):
        self.stack.append(value)
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            return None
        self.size -= 1
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]

    def contains(self, value):
        return value in self.stack

    def isEmpty(self):
        return self.size == 0

    def __repr__(self) -> str:
        stack = self.stack.copy()
        stack.reverse()
        return 'top -> ' + str(stack)
    
    def __str__(self) -> str:
        return repr(self)