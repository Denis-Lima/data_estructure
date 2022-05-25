from typing import Any


class Node():
    def __init__(self, data: Any, next_: 'Node') -> None:
        self.data = data
        self.next = next_


class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.__size = 0

    def __len__(self):
        return self.__size

    def __str__(self) -> str:
        string = []
        node: Node = self.head
        for _ in range(self.__size):
            string.append(str(node.data))
            node = node.next
        return '-->'.join(string)

    def __repr__(self) -> str:
        return str(self)

    def __iter__(self):
        return self.items()

    def insert_first(self, data: Any):
        self.head = Node(data, self.head)
        self.__size += 1

    def remove_first(self) -> Any:
        if self.head is None:
            raise IndexError(f'Cannot remove in list with size {self.__size}')
        node: Node = self.head
        self.head = self.head.next
        self.__size -= 1
        return node.data

    def insert_at(self, index: int, data: Any):
        if index == 0:
            return self.insert_first(data)
        if index < 0 or index >= len(self):
            raise IndexError(f'Index {index} is out of range')

        current_node = self.head
        current_pos = 0
        while current_pos < index - 1:
            current_node = current_node.next
            current_pos += 1
        current_node.next = Node(data, current_node.next)
        self.__size += 1

    def remove_at(self, index: int) -> Any:
        if index == 0:
            return self.remove_first()
        if index < 0 or index >= len(self):
            raise IndexError(f'Index {index} is out of range')

        current_node = self.head
        current_pos = 0
        while current_pos < index - 1:
            current_node = current_node.next
            current_pos += 1
        node = current_node.next
        current_node.next = current_node.next.next
        self.__size -= 1
        return node.data

    def get_first(self) -> Any:
        first = self.head
        if first is not None:
            return first.data
        return first  # None

    def get_last(self) -> Any:
        return self.get(len(self) - 1)

    def get(self, index: int) -> Any:
        if index == 0:
            return self.get_first()
        if index < 0 or index >= len(self):
            raise IndexError(f'Index {index} is out of range')

        current_node = self.head
        current_pos = 0
        while current_pos != index:
            current_node = current_node.next
            current_pos += 1
        return current_node.data

    def empty(self) -> bool:
        return self.__size == 0

    def items(self) -> Any:
        current = self.head
        while current is not None:
            yield current.data
            current = current.next


if __name__ == '__main__':
    lista = LinkedList()
    print('Is empty?', lista.empty())
    print('Size:', len(lista))
    lista.insert_at(0, 1)
    lista.insert_at(0, 999)
    print(lista)
    lista.insert_first(50)
    lista.insert_at(2, 600)
    print(lista)

    print('Removed(last):', lista.remove_at(len(lista) - 1))
    print('Removed(first):', lista.remove_first())
    print(lista)

    lista.insert_at(1, 40)
    lista.insert_at(2, 7)
    print('First:', lista.get_first())
    print('Last:', lista.get_last())
    print('At 2:', lista.get(2))
    print(lista)
    print('Is empty?', lista.empty())
    print('Size:', len(lista))

    print('Iterating over items: ', end='')
    for item in lista.items():
        print(item, end=' ')

    print('\nIterating over items2: ', end='')
    for item in lista:
        print(item, end=' ')
