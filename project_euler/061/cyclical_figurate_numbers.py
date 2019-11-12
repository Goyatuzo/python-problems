def triangle(n: int) -> int:
    return n * (n + 1) / 2

def square(n: int) -> int:
    return n ** 2

def pentagonal(n: int) -> int:
    return n * (3 * n - 1) / 2

def hexagonal(n: int) -> int:
    return n * (2 * n - 1)

def heptagonal(n: int) -> int:
    return n * (5 * n - 3) / 2

def octagonal(n: int) -> int:
    return n * (3 * n - 2)

def solve_first(n: int) -> int:

    # Triangle      45 < n < 140
    # Square        32 < n < 99
    # Pentagonal    26 < n < 81
    # Hexagonal     23 < n < 70
    # Heptagonal    20 < n < 63
    # Octagonal     18 < n < 58



    return 0
