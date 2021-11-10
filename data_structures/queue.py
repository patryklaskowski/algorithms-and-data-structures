from dataclasses import dataclass


@dataclass
class Node:
    value: object
    next: object = None


class Queue:

    def __init__(self):
        self.first = self.last = None
        self.length = 0

    def __str__(self):
        current = self.last
        elements = []
        while current is not None:
            elements.append(str(current.value))
            current = current.next
        elements.append('<empty>')
        return ' -> '.join(elements)

    def enqueue(self, value):
        """
        Add element to end of queue

        q = Queue()     # None
        q.enqueue('a')  # 'a'
        q.enqueue('b')  # 'b' -> 'a'
        q.enqueue('c')  # 'c' -> 'b' -> 'a'
        """
        node = Node(value)
        if self.length == 0:
            self.first = self.last = node
        else:
            node.next = self.last
            self.last = node
        self.length += 1

    def dequeue(self):
        """
        Remove first element

        q = Queue()         # None
        q.enqueue('a')      # 'a'
        q.enqueue('b')      # 'b' -> 'a'
        q.enqueue('c')      # 'c' -> 'b' -> 'a'
        q.dequeue() -> 'a'  # 'c' -> 'b'
        q.dequeue() -> 'b'  # 'c'
        q.dequeue() -> 'c'  # None
        """
        if self.length == 0:
            return None
        else:
            first_value = self.first.value
            current = self.last
            while current is not None:
                if current == self.first:
                    self.first = self.last = None
                elif current.next == self.first:
                    current.next = None
                    self.first = current
                current = current.next
            self.length -= 1
            return first_value

    def peek(self):
        return self.first.value if self.first is not None else None
