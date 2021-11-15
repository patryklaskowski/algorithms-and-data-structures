import unittest

from tasks.fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    def setUp(self) -> None:
        n = 100
        self.output = fizz_buzz(n)

    def test_correct_fizzbuzz(self):
        for idx, value in enumerate(self.output, 1):
            if idx % 3 == 0 and idx % 5 == 0:
                self.assertEqual(value, 'FizzBuzz')

    def test_correct_fizz(self):
        for idx, value in enumerate(self.output, 1):
            if idx % 3 == 0 and not idx % 5 == 0:
                self.assertEqual(value, 'Fizz')

    def test_correct_buzz(self):
        for idx, value in enumerate(self.output, 1):
            if not idx % 3 == 0 and idx % 5 == 0:
                self.assertEqual(value, 'Buzz')

    def test_correct_other(self):
        for idx, value in enumerate(self.output, 1):
            if not idx % 3 == 0 and not idx % 5 == 0:
                self.assertEqual(value, str(idx))
