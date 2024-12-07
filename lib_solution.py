import math
from functools import reduce
from functools import lru_cache


def factorial_reduce(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)


@lru_cache(maxsize=None)
def factorial_memoization(n):
    if n <= 1:
        return 1
    return n * factorial_memoization(n - 1)


def factorial_gamma(n):
    return math.gamma(n + 1)


if __name__ == "__main__":
    print(factorial_reduce(5))
    print(math.factorial(5))
    print(int(factorial_gamma(5)))
