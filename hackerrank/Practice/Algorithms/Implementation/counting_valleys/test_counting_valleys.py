import unittest

from counting_valleys import counting_valleys

class TestCountingValleys(unittest.TestCase):
    def test_problem(self):
        self.assertEqual(1, counting_valleys(8, "UDDDUDUU"))

if __name__ == '__main__':
    unittest.main()

