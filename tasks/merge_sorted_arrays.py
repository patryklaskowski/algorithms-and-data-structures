import unittest


def merge_sorted_arrays(a, b):
    if not isinstance(a, (list, tuple)) or not isinstance(b, (list, tuple)):
        raise ValueError('Both inputs has to be iterable.')

    length_a = len(a)
    length_b = len(b)

    if length_a == 0:
        return b
    if length_b == 0:
        return a

    output = []

    idx_a = 0
    idx_b = 0

    val_a = a[idx_a]
    val_b = b[idx_b]

    while len(output) != (length_a + length_b):
        if val_a < val_b and val_a != float('inf'):
            output.append(val_a)
            idx_a += 1
            val_a = a[idx_a] if idx_a < length_a else float('inf')
        elif val_b < val_a and val_b != float('inf'):
            output.append(val_b)
            idx_b += 1
            val_b = b[idx_b] if idx_b < length_b else float('inf')

    return output
