def counting_rhombi(w: int, h: int) -> int:
    if w < 2 or h < 2:
        return 0

    count = 0

    for width in range(1, w // 2 + 1):
        for height in range(1, h // 2 + 1):
            curr_count = (w - width * 2 + 1) * (h - height * 2 + 1)
            count += curr_count

    return count
	

if __name__ == '__main__':
    (a, b) = list(map(int, input().split(' ')))
    print(counting_rhombi(a, b))
