def counting_rhombi(w, h):
    count = 0
    larger = max(w, h)

    for r in range(1, larger):
        for x in range(w):
            if x - r < 0 or x + r > w:
                continue

            for y in range(h):
                if y - r < 0 or y + r > h:
                    continue

                count += 1
    return count
	

if __name__ == '__main__':
    (a, b) = list(map(int, input().split(' ')))
    print(counting_rhombi(a, b))
