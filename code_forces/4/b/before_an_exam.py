from typing import List, Tuple


def before_an_exam(days: int, total_time: int, reqs: List[Tuple[int, int]]) -> Tuple[str, str]:
    """
    He has to study not less than minTime i and not more than maxTime i hours per each i-th day. 
    """
    times = ''
    for tup in reqs:
        if total_time == 0:
            # Total time hit 0 before each requirement could be met, so
            # he did not follow his parent's instructions.
            return ['NO', '']
        elif tup[1] < total_time:
            # Subtract the largest amount of time possible from pool.
            total_time -= tup[1]
            times = times + f'{tup[1]} '
        else:
            # Total time only has itself remaining as the time
            times = times + f'{total_time} '
            total_time = 0

    # If there is time left over, he did not follow his parent's instructions.
    if total_time > 0:
        return ['NO', '']

    return ['YES', times]