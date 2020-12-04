from typing import List
from pathlib import Path
from os import path

def get_file(fname: str) -> List[str]:
    with open(path.join(Path(__file__).parent, fname), 'r') as f:
        lines = f.readline()

        # Strip out the newlines since it was messing up the number
        return [line.strip() for line in lines]

def passport_one(fname: str):
    pass

def passport_two(fname: str):
    pass