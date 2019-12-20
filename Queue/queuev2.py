class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def peek(self):
        if self.isEmpty():
            return None

        return self.head.data

    def add(self, data):
        node = Node(data)

        if self.tail != None:
            self.tail.next = node

        self.tail = node

        if self.head == None:
            self.head = node


    def remove(self):
        data = self.head.data
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        
        return data


fila = Queue()
print(fila.isEmpty())
fila.add(1)
print(fila.isEmpty())
print(fila.peek())
fila.add(2)
print(fila.peek())
fila.remove()
print(fila.peek())
fila.remove()
print(fila.peek())
