
def ternary_sequence(x0: int, y0: int, z0: int, x1: int, y1: int, z1: int) -> int:
	cum_sum = 0
	total_runs = x0 + y0 + z0 + x1 + y1 + z1

	pass

if __name__ == '__main__':
	t = int(input())

	for _ in range(t):
		x0, y0, z0 = map(int, input().split(' '))
		x1, y1, z1 = map(int, input().split(' '))

		print(ternary_sequence(x0, y0, z0, x1, y1, z1))
