import unittest
import random

from tasks.anagrams import anagrams
from tests.common import random_letters


def generate_anagram_pairs(n):
    """
    Random word and its anagram pair
    """
    for _ in range(n):
        word = ''.join(list(random_letters(random.randint(0, 15))))
        word_anagram = list(word)
        random.shuffle(word_anagram)
        word_anagram = ''.join(word_anagram)
        yield word, word_anagram


def generate_non_anagram_pairs(n):
    """
    Random word pairs
    """
    for _ in range(n):
        word = ''.join(list(random_letters(random.randint(0, 15))))
        non_word_anagram = ''.join(list(random_letters(random.randint(0, 15))))
        yield word, non_word_anagram


class TestAnagrams(unittest.TestCase):

    def test_extreme_cases(self):
        self.assertEqual(anagrams('', ''), True)

    def test_output_for_correct_anagrams(self):
        for word, word_anagram in generate_anagram_pairs(10):
            self.assertEqual(anagrams(word, word_anagram), True)

    def test_output_for_incorrect_anagrams(self):
        for word, non_word_anagram in generate_non_anagram_pairs(10):
            self.assertEqual(anagrams(word, non_word_anagram), False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
