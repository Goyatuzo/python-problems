from copy import deepcopy


def process_opcodes(ints):
    for curr in range(0, len(ints), 4):
        op = ints[curr]

        # If opcode is 99, terminate
        if op == 99:
            break

        idx_one = ints[curr + 1]
        idx_two = ints[curr + 2]
        idx_three = ints[curr + 3]

        val_one = ints[idx_one]
        val_two = ints[idx_two]

        if op == 1:
            updated = val_one + val_two
        elif op == 2:
            updated = val_one * val_two

        # Update destination with new value
        ints[idx_three] = updated

    return ints


def solve_first(ints):
    return process_opcodes(ints)[0]


def solve_second(ints):
    deep = deepcopy(ints)

    for i in range(0, 100):
        for j in range(10):
            ints = deepcopy(deep)

            ints[1] = i
            ints[2] = j

            answer = solve_first(ints)

            if answer == 19690720:
                return (i, j)


if __name__ == "__main__":
    part_one_fuel = 0
    part_two_fuel = 0

    with open('input.txt', 'r') as f:
        line = f.readline()

        values = [int(i) for i in line.split(',')]

        # Part of problem statement
        values[1] = 12
        values[2] = 2

        print('Part 1: ' + str(solve_first(values)))
        values = [int(i) for i in line.split(',')]
        print('Part 2: ' + str(solve_second(values)))
