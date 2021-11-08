"""
Find first element that occurred multiple time
[1, 2, 1, 2] -> 1
['b', 'a', 'c', 'c', 'b'] -> 'c'
"""


def first_recurring_element(values):
    """Solution with time complexity O(n)"""
    if len(values) < 2:
        return

    holder = {}
    for value in values:
        if value not in holder:
            holder[value] = 1
        else:
            return value
