from typing import List

class Customs:
	__group_answers: List[List[str]]
	__current_group: List[str]

	def __init__(self):
		self.__group_answers = []
		self.__current_group = []


	def process_answers(self, answers: str):
		# If a new group is being processed, add to list of groups and start a new one
		if answers == '':
			self.__group_answers.append(self.__current_group)
			self.__current_group = []
			return

		# Otherwise, add the response to the current group
		self.__current_group.append(answers)

	def part_one(self) -> int:
		# When it first runs, the last group doesn't get added
		self.__group_answers.append(self.__current_group)
		self.__current_group = []

		unique_answers = 0

		for group in self.__group_answers:
			concated_answers = ''.join(group)
			# Use sorting to get worst case n lg n, avoid dict
			sorted_answers = sorted(concated_answers)

			group_count = 0
			for i, char in enumerate(sorted_answers):
				# We need a previous character
				if i == 0:
					group_count = 1
					continue

				# If the prev char and curr are the same, it's a duplicate
				if sorted_answers[i - 1] != char:
					group_count += 1

			unique_answers += group_count


		return unique_answers

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