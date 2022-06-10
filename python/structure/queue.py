class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def contains(self, value):
        return value in self.queue

    def is_empty(self):
        return len(self.queue) == 0

    def __repr__(self) -> str:
        return str(self.queue)

    def __str__(self) -> str:
        return str(self.queue)
