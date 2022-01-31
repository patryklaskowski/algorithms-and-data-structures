import unittest

from data_structures.linked_list import Node, LinkedList
from tests.common import random_values


class TestNode(unittest.TestCase):

    def test_value_attribute(self):
        for value in random_values(10):
            n = Node(value)
            self.assertEqual(n.value, value)

    def test_next_attribute(self):
        for value in random_values(10):
            next_n = Node(value)
            n = Node(value, next_n)
            self.assertEqual(n.next.value, value)


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.linked_list = LinkedList()

    def test_initialization(self):
        self.assertIsNone(self.linked_list.head)
        self.assertIsNone(self.linked_list.tail)
        self.assertEqual(self.linked_list.length, 0)

    def test_append_method_with_one_element(self):
        mock_value = 'a'
        self.linked_list.append(mock_value)

        self.assertEqual(self.linked_list.head.value, mock_value)
        self.assertEqual(self.linked_list.tail.value, mock_value)
        self.assertEqual(self.linked_list.length, 1)

    def test_append_method_with_multiple_elements(self):
        mock_values = list(random_values(10))

        for idx, value in enumerate(mock_values, 1):
            self.linked_list.append(value)

            self.assertEqual(self.linked_list.length, idx)
            self.assertEqual(self.linked_list.tail.value, value)
            self.assertEqual(self.linked_list.head.value, mock_values[0])

    def test_prepend_method_with_one_element(self):
        mock_value = 'a'
        self.linked_list.prepend(mock_value)

        self.assertEqual(self.linked_list.head.value, mock_value)
        self.assertEqual(self.linked_list.tail.value, mock_value)
        self.assertEqual(self.linked_list.length, 1)

    def test_prepend_method_with_multiple_values(self):
        mock_values = list(random_values(10))

        for idx, value in enumerate(mock_values, 1):
            self.linked_list.prepend(value)

            self.assertEqual(self.linked_list.length, idx)
            self.assertEqual(self.linked_list.tail.value, mock_values[0])
            self.assertEqual(self.linked_list.head.value, value)

    def test_incorrect_insert_index(self):
        mock_value = 'foo'

        for idx, value in enumerate(random_values(10)):
            with self.assertRaises(IndexError):
                self.linked_list.insert(mock_value, idx)
            self.linked_list.append(value)

    def test_insert_value_when_only_one_element_exists(self):
        mock_first_value = 'foo'
        mock_second_value = 'bar'

        self.linked_list.append(mock_first_value)

        with self.assertRaises(IndexError):
            self.linked_list.insert(mock_second_value, 1)

        self.assertEqual(self.linked_list.tail.value, mock_first_value)
        self.assertEqual(self.linked_list.head.value, mock_first_value)

        self.linked_list.insert(mock_second_value, 0)

        self.assertEqual(self.linked_list.tail.value, mock_first_value)
        self.assertEqual(self.linked_list.head.value, mock_second_value)

    def test_insert_value_to_the_end(self):
        n = 10
        mock_values = list(random_values(n))
        mock_value = 'xyz'

        for value in mock_values:
            self.linked_list.append(value)

        self.assertEqual(self.linked_list.tail.value, mock_values[-1])
        self.assertEqual(self.linked_list.length, n)

        self.linked_list.insert(mock_value, n - 1)

        self.assertEqual(self.linked_list.tail.value, mock_value)
        self.assertEqual(self.linked_list.length, n + 1)

    def test_insert_value_to_the_beginning(self):
        n = 10
        mock_values = list(random_values(n))
        mock_value = 'xyz'

        for value in mock_values:
            self.linked_list.append(value)

        self.assertEqual(self.linked_list.head.value, mock_values[0])
        self.assertEqual(self.linked_list.length, n)

        self.linked_list.insert(mock_value, 0)

        self.assertEqual(self.linked_list.head.value, mock_value)
        self.assertEqual(self.linked_list.length, n + 1)

    def test_insert_value_to_the_middle(self):
        mock_idx = 2
        n = 4
        mock_values = list(random_values(n))
        mock_value = 'xyz'

        for value in mock_values:
            self.linked_list.append(value)

        self.linked_list.insert(mock_value, mock_idx)

        self.assertEqual(n + 1, self.linked_list.length)

        current = self.linked_list.head
        for _ in range(mock_idx):
            current = current.next
        self.assertEqual(current.value, mock_value)

    def test_get_existing_value(self):
        mock_values = list(random_values(10))
        for value in mock_values:
            self.linked_list.append(value)

        for idx, value in enumerate(mock_values):
            self.assertEqual(value, self.linked_list.get(idx))

    def test_get_nonexisting_value(self):
        n = 5
        mock_values = list(random_values(n))
        for value in mock_values:
            self.linked_list.append(value)

        with self.assertRaises(IndexError):
            self.linked_list.get(n + 5)
            self.linked_list.get(n - 5)

    def test_delete_existing_index(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
