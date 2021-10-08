from typing import Any, Union

class Node():
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self) -> str:
        string = []
        node = self.head
        while node:
            string.append(str(node.data))
            node = node.next
        return '[' + ' -> '.join(string) + ']'

    def get_node(self, index) -> Union[Node, None]:
        if not len(self) or index >= len(self) or index < 0:
            raise IndexError('Index is out of range')

        node = self.head
        for i in range(index):
            if not node.next:
                break
            node = node.next
        return node

    def insert(self, index: int, data: Any) -> None:
        if index == 0:
            self.insert_first(data)
            return
        elif index == self.size:
            self.insert_last(data)
            return

        new_node = Node(data)
        previous_node = self.get_node(index - 1)
        new_node.next, previous_node.next = previous_node.next, new_node
        self.size += 1

    def insert_first(self, data: Any) -> None:
        new_node = Node(data)
        if not self.size:
                self.head = new_node
                self.size += 1
                return
        new_node.next, self.head = self.head, new_node
        self.size += 1
    
    def insert_last(self, data: Any) -> None:
        if self.size == 0:
            self.head = Node(data)
            self.size += 1
            return
        node = self.head
        while True:
            if not node.next:
                break
            node = node.next
        node.next = Node(data)
        self.size += 1

    def get_first(self) -> Union[Any, None]:
        return self.get(0)

    def get_last(self) -> Union[Any, None]:
        return self.get(self.size)

    def get(self, index) -> Union[Any, None]:
        node = self.get_node(index)
        if node:
            return node.data
        return node