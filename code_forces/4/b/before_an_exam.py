from typing import List, Tuple


def before_an_exam(days: int, total_time: int, reqs: List[Tuple[int, int]]) -> Tuple[str, str]:
    """
    He has to study not less than minTime i and not more than maxTime i hours per each i-th day.
    """

    # First let's try using all of max
    prospect = [i[1] for i in reqs]

    curr_sum = sum(prospect)


    curr_i = len(prospect) - 1
    while curr_sum > total_time and curr_i >= 0:
        sum_diff = curr_sum - total_time
        necessary = reqs[curr_i][1] - sum_diff

        if necessary >= reqs[curr_i][0] and necessary <= reqs[curr_i][1]:
            prospect[curr_i] = necessary 

            curr_sum += necessary 
            curr_sum -= reqs[curr_i][1]
        else:
            prospect[curr_i] = reqs[curr_i][0]
            # currsum can be recomputed in constant time since we have both values
            curr_sum += reqs[curr_i][0]
            curr_sum -= reqs[curr_i][1]

        curr_i -= 1

    if sum(prospect) != total_time:
        return ['NO', '']
    
    return ['YES', ' '.join([str(i) for i in prospect])]


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