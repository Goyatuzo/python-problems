from math import floor


def solve_first(mass):
    return floor(mass / 3) - 2


if __name__ == "__main__":
    total_fuel = 0

    with open('inputs.txt', 'r') as f:

        line = f.readline()

        while line:
            fuel_req = int(line.strip())
            total_fuel += solve_first(fuel_req)
            line = f.readline()

    print(total_fuel)
