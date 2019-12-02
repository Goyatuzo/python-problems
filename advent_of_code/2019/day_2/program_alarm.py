
def solve_first(ints):
    for curr in range(0, len(ints), 4):
        op = ints[curr]

        if op == 99:
            break

        idx_one = ints[curr + 1]
        idx_two = ints[curr + 2]
        idx_three = ints[curr + 3]

        # Check if any are 99
        if idx_one == 99 or idx_two == 99 or idx_three == 99:
            break

        val_one = ints[idx_one]
        val_two = ints[idx_two]

        if op == 1:
            updated = val_one + val_two
        elif op == 2:
            updated = val_one * val_two

        # Update destination with new value
        ints[idx_three] = updated

    return ints


if __name__ == "__main__":
    part_one_fuel = 0
    part_two_fuel = 0

    with open('input.txt', 'r') as f:
        line = f.readline()

        values = [int(i) for i in line.split(',')]
        print(values)

        print('Part 1: ' + ','.join([str(i) for i in solve_first(values)]))
