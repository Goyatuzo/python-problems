def meets_criteria(num):
    # Cast to string for easier processing
    num = str(num)

    # Keep track of results
    adjacent_digits = False
    is_increasing = True

    previous_digit = num[0]

    for digit in num[1:]:
        if digit == previous_digit:
            adjacent_digits = True
        if int(previous_digit) > int(digit):
            is_increasing = False

        previous_digit = digit

    return adjacent_digits and is_increasing


def meets_criteria_two(num):
    # Cast to string for easier processing
    num = str(num)

    # Keep track of results
    adjacent_count = 0
    adjacent_digits = False

    is_increasing = True

    previous_digit = num[0]

    for digit in num[1:]:

        if adjacent_count == -1:
            pass
        elif digit == previous_digit:
            adjacent_count += 1
            adjacent_digits = True
        else:
            if adjacent_count == 1:
                adjacent_count = -1
            else:
                adjacent_count = 0

        if int(previous_digit) > int(digit):
            is_increasing = False

        previous_digit = digit

    result = (adjacent_count == -1 or adjacent_count == 1) \
        and adjacent_digits \
        and is_increasing

    return result


def solve_first(lo, hi):
    values = [i for i in range(lo, hi + 1) if meets_criteria(i)]

    return values


def solve_second(lo, hi):
    values = [i for i in range(lo, hi + 1) if meets_criteria_two(i)]

    return values


if __name__ == "__main__":
    lo = 278384
    hi = 824795

    print("Part 1: " + str(len(solve_first(lo, hi))))
    print("Part 2: " + str(len(solve_second(lo, hi))))
