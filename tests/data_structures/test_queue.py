import unittest

from data_structures.queue import Node, Queue
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


class TestQueue(unittest.TestCase):

    def setUp(self) -> None:
        self.queue = Queue()

    def tearDown(self) -> None:
        del self.queue

    def test_queue_initialization(self) -> None:
        self.assertEqual(self.queue.first, None)
        self.assertEqual(self.queue.last, None)
        self.assertEqual(self.queue.length, 0)
        self.assertEqual(self.queue.peek(), None)
        self.assertEqual(self.queue.dequeue(), None)
        with self.assertRaises(TypeError):
            self.queue.enqueue()

    def test_adding_elements(self) -> Node:
        mock_values = list(random_values(5))

        for idx, value in enumerate(mock_values, 1):
            self.queue.enqueue(value)
            self.assertEqual(self.queue.first.value, mock_values[0])
            self.assertEqual(self.queue.last.value, value)
            self.assertEqual(self.queue.length, idx)

    def test_removing_elements(self):
        n = 5
        mock_values = list(random_values(n))
        for value in mock_values:
            self.queue.enqueue(value)

        for idx, value in enumerate(mock_values, 1):
            self.assertEqual(self.queue.dequeue(), value)
            self.assertEqual(self.queue.length, n-idx)

    def test_peek_elements(self):
        n = 5
        mock_values = list(random_values(n))

        self.assertEqual(self.queue.peek(), None)
        for value in mock_values:
            self.queue.enqueue(value)
            self.assertEqual(self.queue.peek(), mock_values[0])

        for idx, value in enumerate(mock_values):
            self.assertEqual(self.queue.peek(), mock_values[0+idx])
            self.queue.dequeue()
        # self.assertEqual(self.queue.peek(), None)
