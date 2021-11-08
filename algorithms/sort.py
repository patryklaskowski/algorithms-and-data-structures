import unittest


def bubble_sort(values):
    # Simple
    # O(n^2)
    if len(values) < 2:
        return values

    start_again = True
    while start_again:
        changed = False

        for i in range(len(values) - 1):
            current = values[i]
            _next = values[i+1]
            if current > _next:
                values[i+1] = current
                values[i] = _next
                changed = True

        if not changed:
            start_again = False

    return values


def selection_sort(values):
    # Simple

    length = len(values)

    for i in range(length):

        min_idx = i
        tmp = values[i]

        for j in range(i, length):
            # Find minimum value idx
            if values[j] < values[min_idx]:
                min_idx = j

        values[i] = values[min_idx]
        values[min_idx] = tmp

    return values


def insertion_sort(values):
    # Simple
    pass


def divide(values):
    middle = int(len(values)/2)
    return values[:middle], values[middle:]


def merge_in_order(values_a, values_b):
    result = []
    idx_a = 0
    idx_b = 0
    while (idx_a < len(values_a)) and (idx_b < len(values_b)):
        if values_a[idx_a] < values_b[idx_b]:
            result.append(values_a[idx_a])
            idx_a += 1
        else:
            result.append(values_b[idx_b])
            idx_b += 1
    print('idx_a: ', idx_a, 'idx_b: ', idx_b    )
    return result

print(merge_in_order([20, 5, 9], [3, 4, 6]))


def merge_sort(values):
    pass


def quick_sort(values):
    pass


class TestSortAlgorithms(unittest.TestCase):
    def setUp(self):
        self.mock_values = [5, 3, 8, 2, 1, 4, 9, 6, 7]
        self.expected_output = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_bubble_sort(self):
        self.assertEqual(self.expected_output, bubble_sort(self.mock_values))

    def test_selection_sort(self):
        self.assertEqual(self.expected_output, selection_sort(self.mock_values))

#     def test_insertion_sort(self):
#         self.assertEqual(self.expected_output, insertion_sort(self.mock_values))

#     def test_merge_sort(self):
#         self.assertEqual(self.expected_output, merge_sort(self.mock_values))

#     def test_quick_sort(self):
#         self.assertEqual(self.expected_output, quick_sort(self.mock_values))


class TestHelperFunctions(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(([1, 2, 3], [4, 5, 6]), divide([1, 2, 3, 4, 5, 6]))
        self.assertEqual(([1], [2, 3]), divide([1, 2, 3]))


if __name__ == '__main__':
    unittest.main(verbosity=2)
