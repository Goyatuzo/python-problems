from typing import Dict

db: Dict[str, int] = {}

def registration_system(name: str) -> str:
    if name in db:
        db[name] = db[name] + 1
    else:
        db[name] = 0
        # If it's the first instance, return OK
        return 'OK'

    return f'{name}{db[name]}'

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        print(registration_system(input()))