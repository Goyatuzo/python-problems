
def distance_and_axis(n: int, k: int) -> int:
	if n > k and n % 2 == 1:
		return 1
	elif n > k and n % 2 == 0:
		return 0

	return k - n


if __name__ == '__main__':
	t = int(input())

	for _ in range(t):
		n, k = map(int, input().split(' '))

		print(distance_and_axis(n, k))
