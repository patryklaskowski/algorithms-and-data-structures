import unittest

from data_structures.stack import Node, Stack
from tests.common import random_values


class TestNode(unittest.TestCase):
    def test_node_creation(self):
        with self.assertRaises(TypeError):
            Node()

        for value in random_values(10):
            n = Node(value)
            self.assertEqual(n.value, value)
            self.assertEqual(n.next, None)

    def test_node_next_value_assignment(self):
        """node_a -> node_b -> None"""
        for value_a in random_values(5):
            node_a = Node(value_a)
            self.assertEqual(node_a.value, value_a)
            self.assertEqual(node_a.next, None)

            for value_b in random_values(5):
                node_b = Node(value_b)
                self.assertEqual(node_b.value, value_b)
                self.assertEqual(node_b.next, None)

                node_a.next = node_b
                self.assertEqual(node_a.next, node_b)
                self.assertEqual(node_a.next.value, value_b)
                self.assertEqual(node_a.next.next, None)


class TestStack(unittest.TestCase):

    def setUp(self) -> None:
        self.stack = Stack()

    def test_stack_initialization(self):
        self.assertEqual(self.stack.top, None)
        self.assertEqual(self.stack.bottom, None)
        self.assertEqual(self.stack.length, 0)

    def test_push_method(self):
        for idx, value in enumerate(random_values(10), start=1):
            self.stack.push(value)
            self.assertEqual(self.stack.length, idx)

    def test_peek_method(self):
        self.assertEqual(self.stack.peek(), None)
        for value in random_values(10):
            self.stack.push(value)
            self.assertEqual(self.stack.peek(), value)

    def test_pop_method_with_one_element(self):
        self.assertEqual(self.stack.pop(), None)
        for value in random_values(10):
            self.stack.push(value)
            self.assertEqual(self.stack.top.value, value)
            self.assertEqual(self.stack.pop(), value)

    def test_top_and_bottom_attributes(self):
        mock_values = list(random_values(5))

        self.assertEqual(self.stack.bottom, None)
        self.assertEqual(self.stack.top, None)
        self.assertEqual(self.stack.length, 0)

        for idx, value in enumerate(mock_values, 1):
            self.stack.push(value)
            self.assertEqual(self.stack.length, idx)
            self.assertEqual(self.stack.peek(), value)
            self.assertEqual(self.stack.bottom.value, mock_values[0])
            self.assertEqual(self.stack.top.value, value)

        for value in mock_values[::-1]:
            self.assertEqual(self.stack.pop(), value)

        self.assertEqual(self.stack.bottom, None)
        self.assertEqual(self.stack.top, None)
        self.assertEqual(self.stack.length, 0)



if __name__ == '__main__':
    unittest.main(verbosity=2)
