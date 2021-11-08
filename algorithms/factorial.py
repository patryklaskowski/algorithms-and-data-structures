import unittest


def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n-1)


def factorial_iterative(n):
    ans = 1
    while n >= 1:
        ans *= n
        n -= 1
    return ans


class TestFactorialRecursive(unittest.TestCase):

    def test_correct_solution(self):
        self.assertEqual(factorial_recursive(2), 2) # 2 * 1
        self.assertEqual(factorial_recursive(3), 6) # 3 * 2 * 1
        self.assertEqual(factorial_recursive(4), 24) # 4 * 3 * 2 * 1
        self.assertEqual(factorial_recursive(5), 120) # 5 * 4 * 3 * 2 * 1


class TestFactorialIterative(unittest.TestCase):

    def test_correct_solution(self):
        self.assertEqual(2, factorial_iterative(2)) # 2 * 1
        self.assertEqual(6, factorial_iterative(3)) # 3 * 2 * 1
        self.assertEqual(24, factorial_iterative(4)) # 4 * 3 * 2 * 1
        self.assertEqual(120, factorial_iterative(5)) # 5 * 4 * 3 * 2 * 1


if __name__ == '__main__':
    unittest.main()
