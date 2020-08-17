
def omkar_and_bed_wars(dirs: str) -> int:
    # A bunch of if statements?
    ops = 0

    i = 0

    while i < len(dirs):
        two = dirs[i:i+2]
        three = dirs[i:i+3]
        four = dirs[i:i+4]

        if len(two) == 1:
            i += 1
        elif four == 'RRRL' or four == 'RRRR':
            ops += 1
            i += 4
        elif two == 'RL':
            i += 2
        elif two == 'LL':
            ops += 1
            i += 2
        elif three == 'RRL' or three == 'RLL':
            i += 3
        elif three == 'RRR' or three == 'RLL':
            ops += 1
            i += 3
        elif two == 'RR':
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
