from typing import List
from pathlib import Path
from os import path

def boarding_ticket(ticket: str) -> int:
    row = (0, 128)
    column = (0, 7)

    for char in ticket:
        row_avg = (row[0] + row[1]) / 2
        column_avg = (column[0] + column[1]) / 2
        if char == 'F':
            row = (row_avg, row[1])
        elif char == 'B':
            row = (row[0], row_avg)
        elif char == 'L':
            column = (column[0], column_avg)
        elif char == 'R':
            column = (column[1] / 2, column[1])



if __name__ == "__main__":
    print(f'Part 1: {tobaggan_one("input.txt")}')
    print(f'Part 2: {tobaggan_two("input.txt")}')
