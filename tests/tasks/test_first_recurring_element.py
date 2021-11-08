import unittest

from tasks.first_recurring_element import first_recurring_element


class TestFirstRecurringElement(unittest.TestCase):
    def test_typical_input_with_recurrence(self):
        self.assertEqual(first_recurring_element([1, 2, 3, 2, -4, 5, 1.1, 1]), 2)
        self.assertEqual(first_recurring_element(['a', 'b', 'b', 'a']), 'b')
        self.assertEqual(first_recurring_element([2, None, 'a', None]), None)

    def test_typical_input_without_recurrence(self):
        self.assertEqual(first_recurring_element([1, 2, 3]), None)
        self.assertEqual(first_recurring_element(['a', 'b']), None)
        self.assertEqual(first_recurring_element([2, None, 'a']), None)

    def test_extreme_cases(self):
        self.assertEqual(first_recurring_element([]), None)
        self.assertEqual(first_recurring_element([1]), None)


if __name__ == '__main__':
    unittest.main()
