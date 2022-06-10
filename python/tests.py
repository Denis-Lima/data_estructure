from structure.hash_table import HashMap
from structure.linked_list import LinkedList
from structure.queue import Queue
from structure.stack import Stack

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

print()
print('-' * 40)
stack = Stack()
stack.push(10)
stack.push(3)
print(stack)
print(stack.peek())
print('Empty?', stack.is_empty())
print(stack.pop())
print(stack.pop())

print('-' * 40)
hashmap = HashMap()
hashmap.add('key1', 130)
hashmap['march 6'] = 10
hashmap['march 17'] = 9
print(hashmap.get('key1'))

print(hashmap.arr)
del hashmap['key1']
print(hashmap.arr)

print(hashmap['key1'])
print(hashmap['march 6'])
print(hashmap['march 17'])

print('-' * 40)
fila = Queue()
fila.enqueue(10)
fila.enqueue(100)
print('is empty?', fila.is_empty())
print(fila)
print(fila.peek())
print('contains 10?', fila.contains(10))
print(fila.dequeue())
print(fila.dequeue())
