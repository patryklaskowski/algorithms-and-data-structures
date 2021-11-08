import random
import string


def random_values(n):
    possibilities = {
        'letters': {'call': random.choice, 'args': (string.ascii_letters, )},
        'integers': {'call': random.randint, 'args': (-100, 100)},
        'floats': {'call': random.random, 'args': ()},
        'booleans': {'call': lambda: random.choice([True, False]), 'args': ()}
    }

    for _ in range(n):
        value = random.choice(list(possibilities.values()))
        function = value['call']
        args = value['args']
        yield function(*args)


def random_letters(n):
    for _ in range(n):
        yield random.choice(string.ascii_letters)
