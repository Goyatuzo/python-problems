import unittest

from boarding import boarding_ticket

class TestBoarding(unittest.TestCase):
    def test_given_one(self):
        self.assertEqual(7, boarding_ticket('FF'))

if __name__ == '__main__':
    unittest.main()
