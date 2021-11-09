"""
Stack implementation using linked list.
Stack implementation using arrays is bad idea because of O(n) time complexity
"""
from dataclasses import dataclass


@dataclass
class Node:
    value: object
    next: object = None


class Stack:

    def __init__(self):
        self.top = self.bottom = None
        self.length = 0

    def __str__(self) -> str:
        ground_lvl = '-------------'

        current_lvl = self.bottom
        stack_levels = [ground_lvl]
        while current_lvl is not None:
            stack_levels.append(current_lvl.value)
            current_lvl = current_lvl.next
        return '\n'.join(stack_levels[::-1])

    def push(self, value):
        """Add element on top"""
        n = Node(value)
        if self.length == 0:
            self.top = self.bottom = n
        else:
            self.top.next = n
            self.top = n
        self.length += 1

    def peek(self):
        """Check top value"""
        return self.top.value if self.top is not None else self.top

    def pop(self):
        """Get top value"""
        if self.top is None:
            return None

        top_value = self.top.value

        current = self.bottom
        while current is not None:
            if current == self.top:
                self.bottom = self.top = None
            elif current.next == self.top:
                self.top = current
                current.next = None
            current = current.next

        self.length -= 1
        return top_value

    def empty(self) -> bool:
        return self.length == 0
