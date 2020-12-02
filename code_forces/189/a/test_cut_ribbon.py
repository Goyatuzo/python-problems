import unittest

from cut_ribbon import cut_ribbon

class TestCutRibbon(unittest.TestCase):
    def test_given_one(self):
        self.assertEqual(2, cut_ribbon(5, 5, 3, 2))
    def test_given_two(self):
        self.assertEqual(2, cut_ribbon(7, 5, 5, 2))
    
    def test_inefficient(self):
        """The only possible cut is for a single 5-length"""
        self.assertEqual(1, cut_ribbon(5, 5, 4, 2))



if __name__ == '__main__':
    unittest.main()
