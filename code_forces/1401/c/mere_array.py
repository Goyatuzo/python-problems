from typing import List

def mere_array(arr: List[int]) -> str:
	minimum = min(arr)

	sorted_arr = sorted(arr)

	for i in range(len(arr)):
		if arr[i] != sorted_arr[i]:
			if arr[i] % minimum != 0 or sorted_arr[i] % minimum != 0:
				return 'NO'

	# Reaching this point means all GCDs were found
	return 'YES'

if __name__ == '__main__':
	t = int(input())

	for _ in range(t):
		n = int(input())

		print(mere_array(list(map(int, input().split(' ')))))
