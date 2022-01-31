from dataclasses import dataclass, field


@dataclass
class Node:
    value: object
    next: object = field(repr=False, default=None)


class LinkedList:
    """
    HEAD | a -> b -> c -> None | TAIL
    """

    def __init__(self) -> None:
        self.head = self.tail = None
        self.length = 0

    def __str__(self) -> str:
        """head | 0 -> 1 -> 2 -> 3 -> <empty> | tail"""
        tail = '| tail'
        head = 'head |'
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.value))
            node = node.next
        nodes.append('<empty>')
        return f'{head} {" -> ".join(nodes)} {tail}'

    def append(self, value) -> None:
        """Adds element to the end (tail)."""
        node = Node(value)
        if self.length == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def prepend(self, value) -> None:
        """Ads element at the beginning (head)."""
        node = Node(value)
        if self.length == 0:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def insert(self, value, idx: int) -> None:
        """Insert value on specific index. All values after index are moved by one."""
        node = Node(value)
        if not 0 <= idx <= self.length - 1:
            raise IndexError('Index out of range.')
        if idx == 0:
            self.prepend(value)
        elif idx == self.length - 1:
            self.append(value)
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            node.next = current.next
            current.next = node
            self.length += 1

    def get(self, idx: int) -> None:
        """Return value from index."""
        if not 0 <= idx < self.length:
            raise IndexError('Index out of range.')
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value

    def delete(self, idx: int) -> None:
        """Deletes value from index"""
        if not 0 <= idx < self.length:
            raise IndexError('Index out of range.')
        if idx == 0:
            self.head = self.head.next
        pass
    
    def reverse(self) -> None:
        pass

    def search(self) -> (int, None):
        pass
