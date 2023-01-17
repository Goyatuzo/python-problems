def football(players: str) -> bool:
	consecutive = 0
	prev = ''
	for player in players:
		if prev == player:
			consecutive += 1
		else:
			consecutive = 1
			prev = player

		if consecutive >= 7:
			return True
	return False


if __name__ == '__main__':
	print('YES' if football(input()) else 'NO')