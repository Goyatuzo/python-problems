from math import floor


def solve_first(mass):
    return floor(mass / 3) - 2


def solve_recursive(mass):
    fuel_mass = solve_first(mass)

    if fuel_mass <= 0:
        return 0

    return fuel_mass + solve_recursive(fuel_mass)


if __name__ == "__main__":
    part_one_fuel = 0
    part_two_fuel = 0

    with open('inputs.txt', 'r') as f:

        line = f.readline()

        while line:
            fuel_req = int(line.strip())
            part_one_fuel += solve_first(fuel_req)
            part_two_fuel += solve_recursive(fuel_req)
            line = f.readline()

    print('Part 1: ' + str(part_one_fuel))
    print('Part 2: ' + str(part_two_fuel))
