from math import ceil


def watermelon(number: int) -> str:
    """Want to divide the watermelon in such a way that each of the two parts weighs even number of kilos,
    at the same time it is not obligatory that the parts are equal"""
    # Special case, all even numbers greater than 2 will divide evenly
    if number > 2 and number % 2 == 0:
        return 'YES'

    for i in range(2, int(ceil(number / 2)), 2):
        if number - i > 0 and (number % i) == 0:
            return 'YES'

    return 'NO'


if __name__ == '__main__':
    t = int(input())

    print(watermelon(t))
