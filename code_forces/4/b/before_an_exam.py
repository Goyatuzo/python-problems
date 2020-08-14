from typing import List, Tuple


def before_an_exam(days: int, total_time: int, reqs: List[Tuple[int, int]]) -> Tuple[str, str]:
    """
    He has to study not less than minTime i and not more than maxTime i hours per each i-th day.
    """
    times = ''
    for tup in reqs:
        if tup[1] <= total_time:
            # Subtract the largest amount of time possible from pool.
            total_time -= tup[1]
            times = times + f'{tup[1]} '
        elif tup[0] < total_time:
            # Total time only has itself remaining as the time
            times = times + f'{total_time} '
            total_time = 0

    # If there is time left over or too much taken away, he did not follow his parent's instructions.
    if total_time != 0:
        return ['NO', '']

    return ['YES', times]


if __name__ == '__main__':
    d, sumTime = map(int, input().split())

    requirements = []

    for _ in range(d):
        mi, ma = map(int, input().split())

        requirements.append((mi, ma))

    res = before_an_exam(d, sumTime, requirements)

    print(res[0])
    if res[1] != '':
        print(res[1])