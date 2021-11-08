import unittest
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f'Elapsed time of {func.__name__}({args}, {kwargs}): {round(time.time() - start, 2)}s.')
        return result
    return wrapper


def fibonacci_recursive(n):
    # idx: 0, 1, 2, 3, 4, 5, 6, 7
    # val: 0, 1, 1, 2, 3, 5, 8, 13
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)



def fibonacci_recursive_with_memoization(n, memory={}):

    if memory.get(n, None):
        return memory[n]

    if n == 0:
        return 0
    if n == 1:
        return 1

    ans = fibonacci_recursive_with_memoization(n-1, memory) + fibonacci_recursive_with_memoization(n-2, memory)
    memory[n] = ans
    return ans


class TestFibonacciRecursive(unittest.TestCase):
    def test_correct_solution(self):
        self.assertEqual(0, fibonacci_recursive(0))
        self.assertEqual(1, fibonacci_recursive(1))
        self.assertEqual(1, fibonacci_recursive(2))
        self.assertEqual(2, fibonacci_recursive(3))
        self.assertEqual(3, fibonacci_recursive(4))
        self.assertEqual(5, fibonacci_recursive(5))
        self.assertEqual(8, fibonacci_recursive(6))


class TestFibonacciRecursiveWithMemoization(unittest.TestCase):
    def test_correct_solution(self):
        self.assertEqual(0, fibonacci_recursive_with_memoization(0))
        self.assertEqual(1, fibonacci_recursive_with_memoization(1))
        self.assertEqual(1, fibonacci_recursive_with_memoization(2))
        self.assertEqual(2, fibonacci_recursive_with_memoization(3))
        self.assertEqual(3, fibonacci_recursive_with_memoization(4))
        self.assertEqual(5, fibonacci_recursive_with_memoization(5))
        self.assertEqual(8, fibonacci_recursive_with_memoization(6))


if __name__ == '__main__':
    unittest.main(verbosity=2)
