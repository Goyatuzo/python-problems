def boarding_ticket(ticket: str) -> int:
    row = (0, 128)
    column = (0, 7)

    for char in ticket:
        row_avg = int((row[0] + row[1]) / 2)
        column_avg = int((column[0] + column[1]) / 2)
        if char == 'F':
            row = (row[0], row_avg)
        elif char == 'B':
            row = (row_avg, row[1])
        elif char == 'L':
            column = (column[0], column_avg)
        elif char == 'R':
            column = (column_avg, column[1])

    # Look at the last row char to find the row number
    row = row[0] if ticket[6] == 'F' else row[1]
    column = column[0] if ticket[-1] == 'L' else column[1]

    return row * 8 + column