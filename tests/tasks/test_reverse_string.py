import unittest
import random

from tasks.reverse_string import reverse_inplace, reverse_with_array
from tests.common import random_letters


def generate_reversed_pairs(n):
    """
    Random word and its reversed version pair
    """
    for _ in range(n):
        word = ''.join(list(random_letters(random.randint(0, 15))))
        word_reversed = word[::-1]
        yield word, word_reversed


class TestReverseInplace(unittest.TestCase):
    def test_expected_output(self):
        for word, word_reversed in generate_reversed_pairs(10):
            self.assertEqual(word_reversed, reverse_inplace(word))

    def test_edge_cases(self):
        self.assertEqual('', reverse_inplace(''))
        self.assertEqual('a', reverse_inplace('a'))


class TestReverseWithArray(unittest.TestCase):
    def test_normal_case(self):
        for word, word_reversed in generate_reversed_pairs(10):
            self.assertEqual(word_reversed, reverse_with_array(word))

    def test_edge_cases(self):
        self.assertEqual('', reverse_with_array(''))
        self.assertEqual('a', reverse_with_array('a'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
