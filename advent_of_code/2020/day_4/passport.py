from typing import List
from pathlib import Path
from os import MFD_HUGETLB, path

def get_file(fname: str) -> List[str]:
    with open(path.join(Path(__file__).parent, fname), 'r') as f:
        lines = f.readlines()

        # Strip out the newlines since it was messing up the number
        return [line.strip() for line in lines]

def passport_one(fname: str):
    lst = get_file(fname)

    curr_pass = ''
    valid_passports = 0
    for line in lst:
        if line == '':
            # Get all the current variables
            entries = sorted(curr_pass.split(' '))

            required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
            # BYR
            for entry in entries:                    
                field = entry.split(':')

                try:
                    required.remove(field[0])
                except:
                    pass

            if len(required) == 0:
                valid_passports += 1

            # Reset the accumulator variable
            curr_pass = ''
        else:
            # Add empty space to help with splitting
            curr_pass += line + ' '

    return valid_passports

def passport_two(fname: str):
    return 0

if __name__ == "__main__":
    print(f'Part 1: {passport_one("input.txt")}')
    print(f'Part 2: {passport_two("input.txt")}')