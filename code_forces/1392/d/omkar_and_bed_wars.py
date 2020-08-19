
def omkar_and_bed_wars(dirs: str) -> int:
    # A bunch of if statements?
    ops = 0

    i = 0

    while i < len(dirs):
        two = dirs[i:i+2]
        three = dirs[i:i+3]
        four = dirs[i:i+4]

        if len(two) == 1 and two == 'R':
            i += 1
        elif four == 'RRRL':
            print(f'{four} + 1')
            ops += 1
            i += 4
        elif two == 'RL':
            print(two)
            i += 2
        elif three == 'LLL':
            print(f'{three} + 1')
            ops += 1
            i += 3
        elif two == 'LL':
            print(f'{two} + 1')
            ops += 1
            i += 2
        elif three == 'RRL' or three == 'RLL':
            print(three)
            i += 3
        elif three == 'RRR':
            print(f'{three} + 1')
            ops += 1
            i += 3
        elif two == 'RR':
            print(f'{two} + 1')
            ops += 1
            i += 2
        else:
            i += 1

    return ops


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        s = input()

        print(omkar_and_bed_wars(s))
