from math import floor, ceil

def boarding_ticket(ticket: str) -> int:
    row = (0, 127)
    column = (0, 7)

    for char in ticket:
        row_avg = (row[0] + row[1]) / 2
        column_avg = (column[0] + column[1]) / 2
        if char == 'F':
            row = (row[0], floor(row_avg))
        elif char == 'B':
            row = (ceil(row_avg), row[1])
        elif char == 'L':
            column = (column[0], floor(column_avg))
        elif char == 'R':
            column = (ceil(column_avg), column[1])

    # Look at the last row char to find the row number
    row = row[0] if ticket[6] == 'F' else row[1]
    column = column[0] if ticket[-1] == 'L' else column[1]

    return row * 8 + column

if __name__ == "__main__":
    with open('inputs.txt', 'r') as f:
        line = f.readline().strip()

        max_seat = 0

        while line:
            max_seat = max(max_seat, boarding_ticket(line))
            line = f.readline().strip()


    print(f'Part 1: {max_seat}')