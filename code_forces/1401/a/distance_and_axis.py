
def distance_and_axis(n: int, k: int) -> int:
	# All the 0 cases to prevent division by 0
	if k == 0 and n % 2 == 0:
		return 0
	elif k == 0:
		return 1
	elif n == 0:
		return k

	if k > n:
		return k - n

	b_prelim = (n - k) / 2

	if b_prelim.is_integer():
		return 0
	else:
		return 1



if __name__ == '__main__':
	t = int(input())

	for _ in range(t):
		n, k = map(int, input().split(' '))

		print(distance_and_axis(n, k))
