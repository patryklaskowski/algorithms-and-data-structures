import unittest

# abc -> cba


def reverse_inplace(word):
    if len(word) < 2:
        return word

    letters = list(word)
    length = len(letters)

    for i in range(int(length/2)):
        tmp = letters[i]
        letters[i] = letters[length - 1 - i]
        letters[length - 1 - i] = tmp

    return ''.join(letters)


def reverse_with_array(word):
    if len(word) < 2:
        return word

    _reversed = []
    for i in range(len(word)-1, -1, -1):
        _reversed.append(word[i])

    return ''.join(_reversed)
