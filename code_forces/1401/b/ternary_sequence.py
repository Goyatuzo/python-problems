
def ternary_sequence(x0: int, y0: int, z0: int, x1: int, y1: int, z1: int) -> int:
	cum_sum = 0

	two = min(z0, y1)
	cum_sum = two * 2
	z0 = z0 - two
	y1 = y1 - two

	elim_twos = min(x0, z1)
	z1 -= elim_twos
	x0 -= elim_twos

	elim_twos = min(z0, z1)
	z1 -= elim_twos
	z0 -= elim_twos

	return cum_sum + (-2 * z1)

if __name__ == '__main__':
	t = int(input())

	for _ in range(t):
		x0, y0, z0 = map(int, input().split(' '))
		x1, y1, z1 = map(int, input().split(' '))

		print(ternary_sequence(x0, y0, z0, x1, y1, z1))
