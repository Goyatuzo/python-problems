def counting_rhombi(w: int, h: int) -> int:
    return ((w // 2) * (h // 2)) ** 2
	

if __name__ == '__main__':
    (a, b) = list(map(int, input().split(' ')))
    print(counting_rhombi(a, b))
