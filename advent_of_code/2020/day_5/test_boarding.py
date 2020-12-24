import unittest

from boarding import boarding_ticket

class TestBoarding(unittest.TestCase):
    def test_given_one(self):
        self.assertEqual(357, boarding_ticket('FBFBBFFRLR'))

    def test_given_two(self):
        self.assertEqual(567, boarding_ticket('BFFFBBFRRR'))

    def test_given_three(self):
        self.assertEqual(119, boarding_ticket('FFFBBBFRRR'))

    def test_given_four(self):
        self.assertEqual(820, boarding_ticket('BBFFBBFRLL'))

if __name__ == '__main__':
    unittest.main()
