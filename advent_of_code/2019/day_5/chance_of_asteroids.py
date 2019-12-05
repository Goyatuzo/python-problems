def process_immediate_mode(instruction):
    str_op = str(instruction)
    op_len = len(str_op)

    # If the opcode is only one number, no need to process
    if op_len == 1:
        return (instruction, True, True, True)

    str_op = str_op.zfill(5)
    # Obtain the OP code
    op = int(str_op[3:5])
    # If the first parameter is set to 0, it's in position mode
    one_position = int(str_op[2:3]) == 0
    # If the second parameter is set to 0, it's in position mode
    two_position = int(str_op[1:2]) == 0
    # If the third parameter is set to 0, it's in position mode
    three_position = int(str_op[0:1]) == 0

    return (op, one_position, two_position, three_position)


def process_opcodes(ints):
    curr = 0
    while curr < len(ints):
        op, one_position, two_position, three_position = process_immediate_mode(
            ints[curr])
        # If opcode is 99, terminate
        if op == 99:
            break

        idx_one = ints[curr + 1]

        if op < 3:
            idx_two = ints[curr + 2]
            idx_three = ints[curr + 3]

            # Obtain the second value
            if two_position:
                val_two = ints[idx_two]
            else:
                val_two = idx_two

        # Obtain the first value
        if one_position:
            val_one = ints[idx_one]
        else:
            val_one = idx_one

        # The value to increment curr
        increment = 4

        if op == 1:
            updated = val_one + val_two
        elif op == 2:
            updated = val_one * val_two
        elif op == 3:
            updated = int(input())

            # Update the output address to be the first idx
            idx_three = idx_one
            increment = 2
        elif op == 4:
            if three_position:
                print(ints[idx_one])
            else:
                # In immediate mode, just print out the value
                print(idx_one)
            increment = 2

        # Update destination with new value iff output is set to position
        if three_position:
            ints[idx_three] = updated

        curr += increment

    return ints


if __name__ == "__main__":
    part_one_fuel = 0
    part_two_fuel = 0

    with open('input.txt', 'r') as f:
        line = f.readline()

        values = [int(i) for i in line.split(',')]

        print('Part 1:')
        process_opcodes(values)
        print('END PART 1')
