def phone_numbers(raw_number: str) -> str:
	n = len(raw_number)

	if n % 2 == 0:
		return '-'.join([raw_number[i:i+2] for i in range(0, n, 2)])

	return ''

if __name__ == '__main__':
	print(phone_numbers())