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


def solve_first(lo, hi):
    values = [i for i in range(lo, hi + 1) if meets_criteria(i)]
    
    return values


if __name__ == "__main__":
    print("Part 1: " + str(len(solve_first(278384, 824795))))