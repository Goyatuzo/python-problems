def triangle(n: int) -> int:
    """Triangle 45 < n < 140"""
    return n * (n + 1) / 2


def square(n: int) -> int:
    """Square 32 < n < 99"""
    return n ** 2


def pentagonal(n: int) -> int:
    """Pentagonal 26 < n < 81"""
    return n * (3 * n - 1) / 2


def hexagonal(n: int) -> int:
    """Hexagonal 23 < n < 70"""
    return n * (2 * n - 1)


def heptagonal(n: int) -> int:
    """Heptagonal 20 < n < 63"""
    return n * (5 * n - 3) / 2


def octagonal(n: int) -> int:
    """Octagonal 18 < n < 58"""
    return n * (3 * n - 2)


def solve_first(n: int) -> int:
    return 0
