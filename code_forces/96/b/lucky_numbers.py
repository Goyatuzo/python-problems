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
			numbers.append(candidate)


	return numbers

def lucky_numbers(number: str) -> str:
	luckies = generate_super_lucky_numbers(9)

	return ''

if __name__ == '__main__':
	print(lucky_numbers())