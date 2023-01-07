from typing import List

def progress_bar(nums: List[int]) -> str:
	[n, k, t] = nums
	bar = ['' for _ in range(n)]
	remaining = n * k * t / 100

	for i in range(n):
		if remaining >= k:
			bar[i] = str(k)
		elif remaining < k:
			bar[i] = str(int(remaining))
		else:
			bar[i] = str(0)

		remaining = max(0, remaining - k)

	return bar


if __name__ == '__main__':
	print(" ".join(progress_bar([int(num) for num in input().split()])))
