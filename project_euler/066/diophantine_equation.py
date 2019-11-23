from math import sqrt


def valid_d(max_d: int):
    return [d for d in range(max_d + 1) if not sqrt(d).is_integer()]


def solve_first(max_d: int):

    max_x = 0
    highest_d = 0

    for d in valid_d(max_d):
        x = 2


        y_squared = ((x ** 2) - 1) / d

        while not round(sqrt(y_squared), 5).is_integer():
            x += 1
            y_squared = ((x ** 2) - 1) / d

        if x > max_x:
            max_x = x
            highest_d = d
        print((d, x))

    return (max_x, highest_d)


if __name__ == "__main__":
    print(solve_first(1000))
