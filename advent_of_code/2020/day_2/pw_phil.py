
def pw_phil_valid(line: str) -> bool:
    # Split into three tokens by space
    counts, letter, pw = line.split(' ')

    # Get min and max of the letter
    minimum, maximum = [int(v) for v in counts.split('-')]

    # Get the letter to be evaluated
    letter = letter[0]

    occurance = pw.count(letter)

    return occurance >= minimum and occurance <= maximum

if __name__ == "__main__":
    lst = []
    valid_count = 0

    with open('inputs.txt', 'r') as f:
        line = f.readline()

        while line:
            if pw_phil_valid(line):
                valid_count += 1

            line = f.readline()

    print(f'Part 1: {valid_count}')
