import unittest
import string

from data_structures.hash_table import HashTable
from tests.common import random_letters


class TestHashTable(unittest.TestCase):

    def setUp(self) -> None:
        self.mock_length = 10
        self.hash_table = HashTable(self.mock_length)

    def tearDown(self) -> None:
        del self.hash_table

    def test_length_attribute(self):
        self.assertEqual(self.hash_table.length, self.mock_length)

    def test_inserting_values(self):
        for letter in random_letters(10):
            self.hash_table[letter] = letter
            self.assertEqual(self.hash_table[letter], letter)

    def test_override_existing_key_value_pair(self):
        mock_key = 'foo'
        values = ['foo', 'bar', None, False, 1234]

        for mock_value in values:
            self.hash_table[mock_key] = mock_value
            self.assertEqual(self.hash_table[mock_key], mock_value)

    def test_key_retrieval_method(self):
        for char in string.ascii_letters:
            self.hash_table[char] = 'bar'

        keys = self.hash_table.keys()
        self.assertIsInstance(keys, list)

        for char in string.ascii_letters:
            self.assertTrue(char in keys)

    def test_value_retrieval_method(self):
        for char in string.ascii_letters:
            self.hash_table[char] = char

        values = self.hash_table.values()
        self.assertIsInstance(values, list)

        for char in string.ascii_letters:
            self.assertTrue(char in values)

    def test_cleaning_up_object(self):
        for char in string.ascii_letters:
            self.hash_table[char] = char
        self.hash_table.clear()
        self.assertEqual(len(self.hash_table.keys()), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
