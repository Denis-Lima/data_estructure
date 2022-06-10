from typing import Any, Union


class Node():
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None
        self.preview = None

    def __str__(self) -> str:
        prev = str(self.preview) if not self.preview else str(
            self.preview.data)
        next_ = str(self.next) if not self.next else str(self.next.data)
        return prev + ' <- ' + str(self.data) + ' -> ' + next_

    def __repr__(self) -> str:
        return str(self)


class DoublyLinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self) -> str:
        string = []
        node: Node = self.head
        for _ in range(self.size):
            string.append(str(node.data))
            node = node.next
        return '[' + ' <-> '.join(string) + ']'

    def __repr__(self) -> str:
        return str(self)

    def empty(self) -> bool:
        return self.size == 0

    def get_node(self, index) -> Union[Node, None]:
        if self.empty() or index >= len(self) or index < 0:
            raise IndexError('Index is out of range')

        node = self.head
        for _ in range(index):
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
        new_node.next, previous_node.next, new_node.preview = previous_node.next, new_node, previous_node
        index_node = new_node.next
        index_node.preview = new_node

        self.size += 1

    def insert_first(self, data: Any) -> None:
        new_node = Node(data)
        if self.empty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        new_node.next, self.head.preview, self.head = self.head, new_node, new_node
        self.size += 1

    def insert_last(self, data: Any) -> None:
        new_node = Node(data)
        if self.empty():
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        index_node = self.tail
        new_node.preview, new_node.next, index_node.next = index_node, index_node.next, new_node
        self.tail = new_node
        self.size += 1

    def get_first(self) -> Union[Any, None]:
        first = self.head
        if first:
            return first.data
        return first  # None

    def get_last(self) -> Union[Any, None]:
        last = self.tail
        if last:
            return last.data
        return last  # None

    def get(self, index) -> Union[Any, None]:
        node = self.get_node(index)
        if node:
            return node.data
        return node  # None

    def items(self) -> Node:
        current = self.head
        while current:
            yield current
            current = current.next

    def remove_first(self) -> Node:
        if self.empty():
            raise IndexError('Index is out of range')
        removed = self.head
        self.head = self.head.next
        if self.head:
            self.head.preview = None
        removed.next = None
        self.size -= 1
        return removed

    def remove_last(self) -> Node:
        return self.remove(self.size - 1)

    def remove(self, index: int) -> Node:
        if index >= self.size:
            raise IndexError('Index is out of range')

        if index == 0:
            return self.remove_first()

        preview_node = self.get_node(index - 1)
        removed = preview_node.next
        if removed.next:
            next_node = removed.next
            preview_node.next, next_node.preview, removed.next, removed.preview = next_node, preview_node, None, None
        else:
            preview_node.next = None
            removed.preview = None
        self.size -= 1
        return removed
