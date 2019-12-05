def process_opcodes(ints):
    curr = 0
    while curr < len(ints):
        op = ints[curr]
        # If opcode is 99, terminate
        if op == 99:
            break

        idx_one = ints[curr + 1]

        if op < 3:
            idx_two = ints[curr + 2]
            idx_three = ints[curr + 3]
            val_two = ints[idx_two]

        val_one = ints[idx_one]

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
            print(ints[idx_one])
            increment = 2

        # Update destination with new value
        ints[idx_three] = updated

        curr += increment

    return ints


if __name__ == "__main__":
    print(process_opcodes([3, 0, 4, 0, 99]))
