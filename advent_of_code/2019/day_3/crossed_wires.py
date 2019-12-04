def create_line(curr, cmd):
    coords = {}
    direction = cmd[0]
    amount = int(cmd[1:])

    if direction == 'U':
        for i in range(amount):
            curr = (curr[0], curr[1] + 1)
            coords[curr] = True

    elif direction == 'R':
        for i in range(amount):
            curr = (curr[0] + 1, curr[1])
            coords[curr] = True
    elif direction == 'D':
        for i in range(amount):
            curr = (curr[0], curr[1] - 1)
            coords[curr] = True
    elif direction == 'L':
        for i in range(amount):
            curr = (curr[0] - 1, curr[1])
            coords[curr] = True

    return coords


def get_new_coords(curr, cmd):
    if cmd[0] == 'U':
        curr = (curr[0], curr[1] + int(cmd[1:]))
    elif cmd[0] == 'R':
        curr = (curr[0] + int(cmd[1:]), curr[1])
    elif cmd[0] == 'D':
        curr = (curr[0], curr[1] - int(cmd[1:]))
    elif cmd[0] == 'L':
        curr = (curr[0] - int(cmd[1:]), curr[1])

    return curr


def create_coords(cmds):
    coords = {}
    curr = (0, 0)
    for cmd in cmds:
        coords.update(create_line(curr, cmd))
        curr = get_new_coords(curr, cmd)

    return coords


def solve_first(first_wire, second_wire):
    commands = first_wire.split(',')

    overlap = []

    # Wire 1
    coords_one = create_coords(commands)

    curr = (0, 0)
    for cmd in second_wire.split(','):
        to_next = create_line(curr, cmd)

        for point in to_next:
            if point in coords_one:
                overlap.append(point)

        curr = get_new_coords(curr, cmd)

    # Find the tuple with the smallest manhattan distance
    min_distance = min(overlap, key=lambda coord: abs(
        coord[0]) + abs(coord[1]))

    # Add x and y
    return abs(min_distance[0]) + abs(min_distance[1])


if __name__ == "__main__":
    first_wire = ""
    second_wire = ""

    with open('input.txt', 'r') as f:
        [first_wire, second_wire] = f.readlines()

    print(solve_first(first_wire, second_wire))
