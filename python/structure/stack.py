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

if __name__ == '__main__':
    stack = Stack()
    print(stack)
    print('Popped:', stack.pop())
    print('Peek:', stack.peek())
    stack.push(10)
    stack.push(20)
    print('Peek:', stack.peek())
    stack.push(5)
    stack.push(7)
    print(stack)
    print('Popped:', stack.pop())
    print(stack)
    print('Popped:', stack.pop())
    print('Peek:', stack.peek())
    print(stack)
    stack.push(100)
    stack.push(1)
    print('Peek:', stack.peek())
    stack.push(0)
    print(stack.contains(100))
    print(stack.contains(99))
    print(stack)
