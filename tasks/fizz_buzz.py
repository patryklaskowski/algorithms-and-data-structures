"""
Print integers 1 to N, but print
“Fizz” if an integer is divisible by 3,
“Buzz” if an integer is divisible by 5, and
“FizzBuzz” if an integer is divisible by both 3 and 5.
"""


def fizz_buzz(n):
    output = []
    for i in range(1, n + 1):
        value = ''
        if i % 3 == 0:
            value += 'Fizz'
        if i % 5 == 0:
            value += 'Buzz'
        if value == '':
            value += str(i)
        output.append(value)
    return output
