def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n-1)


def factorial_iterative(n):
    ans = 1
    while n >= 1:
        ans *= n
        n -= 1
    return ans