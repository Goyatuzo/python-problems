from collections import deque
from typing import List

def is_super_lucky(number: str) -> bool:
	fours = 0
	sevens = 0

	for digit in number:
		if digit == '4':
			fours += 1
		elif digit == '7':
			sevens += 1
			
	return fours == sevens and sevens > 0

def generate_super_lucky_numbers(n: int) -> List[int]:
	numbers = []
	queue = deque([''])

	while queue:
		candidate = queue.pop()

		if len(candidate) <= n:
			queue.appendleft(candidate + '4')
			queue.appendleft(candidate + '7')

		if is_super_lucky(candidate):
			numbers.append(int(candidate))


	return numbers


def binary_search(numbers: List[int], target: int) -> int:
	lo = 0
	hi = len(numbers) - 1
	mid = 0
	answer = 0

	while lo <= hi:
		mid = int((lo + hi) / 2)

		if numbers[mid] < target:
			lo = mid + 1
		else:
			answer = numbers[mid]
			hi = mid - 1

	return answer

def lucky_numbers(number: str) -> str:
	luckies = generate_super_lucky_numbers(9)
	return str(binary_search(luckies, int(number)))

if __name__ == '__main__':
	print(lucky_numbers('4900'))