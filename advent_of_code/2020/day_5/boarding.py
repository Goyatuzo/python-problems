from math import floor, ceil

def boarding_ticket(ticket: str) -> int:
    """Calculates the seat ID via the given instructions.
    The row and column is calculated by computing the average and the applying
    the floor or ceiling function. If the value is the lower bound, we apply ceil.
    If it's the upper bound, the floor is applied."""
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

class BoardingSeats:
    def __init__(self):
        # Total number of seats, given we have 127 rows and 7 columns.
        self.empty_seats = [True] * (127 * 8 + 7)

    def fill_seat(self, seat_id: int):
        self.empty_seats[seat_id] = False

    def get_empty_seat(self) -> int:
        # Ignore the first and last row
        for seat_id in range(8, 126 * 8 + 7):
            if self.empty_seats[seat_id] \
               and self.empty_seats[seat_id - 1] is False \
               and self.empty_seats[seat_id + 1] is False:
                return seat_id

        # If no seats could be found, return -1
        return -1


if __name__ == "__main__":
    seats = BoardingSeats()

    with open('inputs.txt', 'r') as f:
        line = f.readline().strip()

        max_seat = 0

        while line:
            curr_seat = boarding_ticket(line)
            max_seat = max(max_seat, curr_seat)
            seats.fill_seat(curr_seat)
            line = f.readline().strip()


    print(f'Part 1: {max_seat}')
    print(f'Part 2: {seats.get_empty_seat()}')