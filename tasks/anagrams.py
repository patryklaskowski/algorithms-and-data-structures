"""
Determine if two words are anagrams

func('patryk', 'krypta') -> True
func('patryk', 'kot') -> False
"""


def anagrams(word_a='', word_b=''):
    """
    O(N)
    """

    if len(word_a) != len(word_b):
        return False

    letters = {}
    for letter in word_a:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

    for letter in word_b:
        if letter in letters:
            letters[letter] -= 1
        else:
            return False

    for value in letters.values():
        if value != 0:
            return False

    return True
