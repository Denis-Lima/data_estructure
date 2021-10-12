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

if __name__ == '__main__':
    queue = Queue()
    print(queue)
    print('Dequeued:', queue.dequeue())
    print('Peek:', queue.peek())
    queue.enqueue(10)
    queue.enqueue(20)
    print('Peek:', queue.peek())
    queue.enqueue(5)
    queue.enqueue(7)
    print(queue)
    print('Dequeued:', queue.dequeue())
    print(queue)
    print('Dequeued:', queue.dequeue())
    print('Peek:', queue.peek())
    print(queue)
    queue.enqueue(100)
    queue.enqueue(1)
    print('Peek:', queue.peek())
    queue.enqueue(0)
    print(queue.contains(100))
    print(queue.contains(99))
    print(queue)