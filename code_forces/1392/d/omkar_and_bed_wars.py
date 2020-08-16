
def omkar_and_bed_wars(dirs: str) -> int:
    # A bunch of if statements?
    ops = 0

    i = 0

    while i < len(dirs):
        # Special cases for beginning and end
        if (i == 0 or i == len(dirs) - 2) and (dirs[i:i+2] == 'LR'):
            i += 2
            continue
        if (i == len(dirs) - 1 and dirs[i] == 'R'):
            break

        three = dirs[i:i+3]

        # RRL is ok
        if three == 'RRL' or three == 'RLL':
            i += 3
            continue

        two = dirs[i:i+2]

        if two != 'RL':
            ops += 1
            i += 2
            continue

        i += 2

    return ops


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        s = input()

        print(omkar_and_bed_wars(s))
