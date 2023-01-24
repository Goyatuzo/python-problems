def phone_numbers(raw_number: str) -> str:
	n = len(raw_number)

	if n % 2 == 0:
		return '-'.join([raw_number[i:i+2] for i in range(0, n, 2)])

	# Odd case here
	last_three = raw_number[-3:]
	rest = raw_number[:-3]

	return '-'.join([rest[i:i+2] for i in range(0, len(rest), 2)]) + f'-{last_three}'

if __name__ == '__main__':
	input()
	print(phone_numbers(input()))