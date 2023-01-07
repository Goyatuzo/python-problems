from typing import List

def progress_bar(nums: List[int]) -> str:
	[n, k, t] = nums
	bar = [0 for _ in range(n)]

	for i in range(n):
		print(t, k, t - k)
		if t > k:
			bar[i] = k
		elif t > 0:
			bar[i] = t
		else:
			bar[i] = 0
		t = max(0, t - k)

	return bar


if __name__ == '__main__':
	for _ in range(n):
		print(progress_bar([int(num) for num in input().split()]))
