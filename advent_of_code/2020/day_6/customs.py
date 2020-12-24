from math import floor, ceil

class Customs:
	answered_yes: int
	def __init__(self):
		self.__answered_yes = 0

	def process_answers(self, answers: str):
		self.__answered_yes += len(answers)

	def part_one(self) -> int:
		return self.__answered_yes

if __name__ == '__main__':
	customs = Customs()

	with open('inputs.txt', 'r') as f:
		line = f.readline()

		while line:
			# Strip in here so that the while loop doesn't get tripped
			line = line.strip()
			customs.process_answers(line)
			line = f.readline()


	print(f'Part 1: {customs.part_one()}')