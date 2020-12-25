import unittest

from customs import Customs

class TestBoarding(unittest.TestCase):
	def test_given_one(self):
		customs = Customs()
		customs.process_answers('abc')
		self.assertEqual(3, customs.part_one())

		customs.process_answers('')
		self.assertEqual(3, customs.part_one())

		customs.process_answers('a')
		self.assertEqual(4, customs.part_one())

	def test_given_two(self):
		customs = Customs()
		customs.process_answers('abc')
		customs.process_answers('a')
		self.assertEqual(1, customs.part_two())

if __name__ == '__main__':
    unittest.main()
