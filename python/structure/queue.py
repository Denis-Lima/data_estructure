class Queue():
    def __init__(self):
        self.queue = []
        self.size = 0

    def enqueue(self, value):
        self.queue.append(value)
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            return None
        self.size -= 1
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return None
        return self.queue[0]

    def contains(self, value):
        return value in self.queue

    def isEmpty(self):
        return self.size == 0

    def __repr__(self) -> str:
        return str(self.queue)

    def __str__(self) -> str:
        return str(self.queue)