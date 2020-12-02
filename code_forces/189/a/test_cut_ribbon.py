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

    def test_code_forces(self):
        self.assertEqual(11, cut_ribbon(3119, 3515, 1021, 7))
        self.assertEqual(1, cut_ribbon(1, 1, 1, 1))
        self.assertEqual(4000, (cut_ribbon(4000, 1, 2, 3)))

    def test_ones(self):
        self.assertEqual(10, cut_ribbon(10, 1, 2, 3))
        self.assertEqual(2, cut_ribbon(2, 1, 1, 1))
        self.assertEqual(5, cut_ribbon(10, 50, 2, 30))
        self.assertEqual(5, cut_ribbon(11, 2, 3, 5))




if __name__ == '__main__':
    unittest.main()
