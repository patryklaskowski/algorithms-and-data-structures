import unittest

from tasks.merge_sorted_arrays import merge_sorted_arrays


class TestMergeSortedArrays(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(merge_sorted_arrays([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_sorted_arrays([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge_sorted_arrays([4, 5, 6], [1, 2, 3]), [1, 2, 3, 4, 5, 6])

        self.assertEqual([1, 2, 4, 5, 6], merge_sorted_arrays([1, 2], [4, 5, 6]))

    def test_edge_case(self):
        self.assertEqual(merge_sorted_arrays([], []), [])
        self.assertEqual(merge_sorted_arrays([1], []), [1])
        self.assertEqual(merge_sorted_arrays([], [1]), [1])

    def test_not_iterable_input(self):
        with self.assertRaises(ValueError):
            merge_sorted_arrays(None, None)


if __name__ == '__main__':
    unittest.main(verbosity=2)
