from typing import List

def mere_array(arr: List[int]) -> str:
	pass

if __name__ == '__main__':
	t = int(input())

	for _ in range(t):
		n = int(input())

		print(mere_array(map(int, input().split(' '))))
