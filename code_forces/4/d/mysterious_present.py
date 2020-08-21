from typing import List, Tuple

def mysterious_present(w: int, h: int, envelopes: List[Tuple[int, int]]) -> Tuple[int, str]:
    # Attach original index to each envelope, and filter out non-conformers
    envs = [(i + 1, dims) for i, dims in enumerate(envelopes) if dims[0] > w and dims[1] > h]
    # Now sort the envelopes
    envs = sorted(envs, key=lambda env: (env[1][0], env[1][1]))
    
    # Store the chains in here
    chain = [(0, el) for el in envs]
    # Set first element in chain to 1
    chain[0] = (1, chain[0][1])
    
    for i in range(len(envs)):
        for j in range(i, len(envs)):
            



if __name__ == '__main__':
    n, w, h = map(int, input().split(' '))

    envelopes = []
    for _ in range(n):
        env_w, env_h = map(int, input().split(' '))
        envelopes.append((env_w, env_h))

    res = mysterious_present(w, h, envelopes)
    print(res[0])
    print(res[1])
