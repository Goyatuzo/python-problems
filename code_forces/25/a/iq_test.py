from typing import List

def iq_test(numbers: List[int]) -> int:
	evens = 0
	odds = 0

	first_even = -1
	first_odd = -1

	for i, num in enumerate(numbers):
		if num % 2 == 0:
			evens += 1
			
			if first_even < 0:
				first_even = i
		else:
			odds += 1

			if first_odd < 0:
				first_odd = i

	return first_even + 1 if evens == 1 else first_odd + 1

if __name__ == '__main__':
	_ = input()
	print(iq_test([int(i) for i in input().split(' ')]))