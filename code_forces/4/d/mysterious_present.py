from typing import List, Tuple

def mysterious_present(w: int, h: int, envelopes: List[Tuple[int, int]]) -> Tuple[int, str]:
    # Attach original index to each envelope
    envs = [(i + 1, dims) for i, dims in enumerate(envelopes)]
    # Now sort the envelopes
    envs = sorted(envs, key=lambda env: (env[1][0], env[1][1]))

    chain = []
    prev = (-1, -1)

    for idx, dims in envs:
        if (prev[0] >= dims[0] or prev[1] >= dims[1]) or (dims[0] <= w or dims[1] <= h):
            continue

        chain.append(str(idx))
        prev = dims

    return (len(chain), ' '.join(chain))

if __name__ == '__main__':
    n, w, h = map(int, input().split(' '))

    envelopes = []
    for _ in range(n):
        env_w, env_h = map(int, input().split(' '))
        envelopes.append((env_w, env_h))

    res = mysterious_present(w, h, envelopes)
    print(res[0])
    print(res[1])