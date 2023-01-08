def domino_piling(m: int, n: int) -> int:
	return int((m * n) / 2)

if __name__ == '__main__':
	[m, n] = [int(s) for s in input().split()]
	print(domino_piling(m, n))