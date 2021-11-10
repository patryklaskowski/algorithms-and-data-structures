import unittest

from tasks.factorial import factorial_recursive, factorial_iterative


class TestFactorialRecursive(unittest.TestCase):

    def test_correct_solution(self):
        self.assertEqual(factorial_recursive(2), 2)  # 2 * 1 = 2
        self.assertEqual(factorial_recursive(3), 6)  # 3 * 2 * 1 = 6
        self.assertEqual(factorial_recursive(4), 24)  # 4 * 3 * 2 * 1 = 24
        self.assertEqual(factorial_recursive(5), 120)  # 5 * 4 * 3 * 2 * 1 = 120


class TestFactorialIterative(unittest.TestCase):

    def test_correct_solution(self):
        self.assertEqual(2, factorial_iterative(2))  # 2 * 1 = 2
        self.assertEqual(6, factorial_iterative(3))  # 3 * 2 * 1 = 6
        self.assertEqual(24, factorial_iterative(4))  # 4 * 3 * 2 * 1 = 24
        self.assertEqual(120, factorial_iterative(5))  # 5 * 4 * 3 * 2 * 1 = 120


if __name__ == '__main__':
    unittest.main()
