from typing import List, Tuple


def mysterious_present(w: int, h: int, envelopes: List[Tuple[int, int]]) -> Tuple[int, str]:
    # Attach original index to each envelope, and filter out non-conformers
    envs = [(i + 1, dims)
            for i, dims in enumerate(envelopes) if dims[0] > w and dims[1] > h]

    # Now sort the envelopes
    xenvs = sorted(envs, key=lambda env: (env[1][0], env[1][1]))
    yenvs = sorted(envs, key=lambda env: (env[1][0], env[1][1]))

    chain = [[None] * len(envs)]] * len(envs)
    curr_dim = (w, h)


    for env in xenvs:
        if curr_dim[0] < env[1][0] and curr_dim[1] < env[1][1]:
            chain.append(env[0])
            curr_dim = env[1]
        
    return len(chain), ' '.join(map(str, chain))

if __name__ == '__main__':
    n, w, h = map(int, input().split(' '))

    envelopes = []
    for _ in range(n):
        env_w, env_h = map(int, input().split(' '))
        envelopes.append((env_w, env_h))

    res = mysterious_present(w, h, envelopes)
    print(res[0])
    print(res[1])
