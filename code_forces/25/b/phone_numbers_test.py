import unittest

from phone_numbers import phone_numbers as foo

class Testphone_numbers(unittest.TestCase):
	def test_given_1(self):
		self.assertEqual(foo('549871'), '54-98-71')

	def test_given_2(self):
		self.assertEqual(foo('1198733'), '11-98-733')

	def test_edge_1(self):
		self.assertEqual(foo('1234'), '12-34')

	def test_edge_2(self):
		self.assertEqual(foo('12345'), '12-345')


if __name__ == '__main__':
    unittest.main()
