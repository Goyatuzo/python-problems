from typing import List, Tuple

def mysterious_present(w: int, h: int, envelopes: List[Tuple[int, int]]) -> Tuple[int, str]:
    # Attach original index to each envelope, and filter out non-conformers
    envs_filtered = [(i, dims) for i, dims in enumerate(envelopes) if dims[0] > w and dims[1] > h]
    # Now sort the envelopes
    envs = sorted(envs_filtered, key=lambda env: (env[1][0], env[1][1]))
    
    # The chain begins with the first value
    chain = [[el[0]] for el in envs]
    
    for i in range(len(envs)):
        curr = envs[i]
        compar = envs_filtered[i]

        if compar[0] < curr[0] and compar[1] < curr[1]:
            chain[i].append(curr[0])
        else:
            chain[i].pop()
            chain[i].append(curr[0])
           
        print(chain[i])

    return (len(chain), ' '.join(list(map(str, chain[-1]))))



if __name__ == '__main__':
    n, w, h = map(int, input().split(' '))

    envelopes = []
    for _ in range(n):
        env_w, env_h = map(int, input().split(' '))
        envelopes.append((env_w, env_h))

    res = mysterious_present(w, h, envelopes)
    print(res[0])
    print(res[1])
