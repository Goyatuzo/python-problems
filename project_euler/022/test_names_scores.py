import unittest

from names_scores import *

class TestNamesScores(unittest.TestCase):
    def test_name(self):
        self.assertEqual(53, quantify_name('COLIN', 1))

    def test_row(self):
        self.assertEqual(49714, quantify_name('COLIN', 938))

if __name__ == '__main__':
    unittest.main()