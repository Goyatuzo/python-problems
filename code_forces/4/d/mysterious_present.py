
from typing import List, Tuple

def mysterious_present(n: int, w: int, h: int, vals: List[Tuple[int, int]]) -> Tuple[str]:
    envelopes = [(i, env) for i, env in enumerate(vals) if env[0] > w and env[1] > h]

    print(envelopes)
    pass