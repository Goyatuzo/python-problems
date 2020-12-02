def pw_phil_splitter(line: str):
    # Split into three tokens by space
    counts, letter, pw = line.split(' ')

    # Get min and max of the letter
    minimum, maximum = [int(v) for v in counts.split('-')]

    # Get the letter to be evaluated
    letter = letter[0]

    return minimum, maximum, letter, pw


def pw_phil_valid(line: str) -> bool:
    minimum, maximum, letter, pw = pw_phil_splitter(line)

    occurance = pw.count(letter)

    return occurance >= minimum and occurance <= maximum


def pw_phil_valid_two(line: str) -> bool:
    begin, end, let, pw = pw_phil_splitter(line)

    first = pw[begin - 1] == let
    second = pw[end - 1] == let

    # EXACTLY 1 occurance must happen
    return (first and not second) or (not first and second)

if __name__ == "__main__":
    lst = []
    valid_count = 0
    valid_two_count = 0

    with open('inputs.txt', 'r') as f:
        line = f.readline()

        while line:
            if pw_phil_valid(line):
                valid_count += 1

            if pw_phil_valid_two(line):
                valid_two_count += 1

            line = f.readline()

    print(f'Part 1: {valid_count}')
    print(f'Part 2: {valid_two_count}')
