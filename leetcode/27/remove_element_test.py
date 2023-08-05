import unittest

from remove_element import remove_element as foo

class Test_Remove_Element(unittest.TestCase):
	def test_given_1(self):
        self.assertEqual(foo([2, 2, 3, 3], 3), 2)

	def test_given_2(self):
        self.assertEqual(foo([0, 1, 4, 0, 3, 2, 2, 2], 2), 5)


if __name__ == '__main__':
    unittest.main()
