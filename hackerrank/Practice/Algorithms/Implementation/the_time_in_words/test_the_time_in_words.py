import unittest

from the_time_in_words import timeInWords

class TestTheTimeInWords(unittest.TestCase):
    def test_given(self):
        self.assertEqual('thirteen minutes to six', timeInWords(5, 47))
        self.assertEqual('three \'o clock', timeInWords(3, 0))
        self.assertEqual('quarter past seven', timeInWords(7, 15))

if __name__ == '__main__':
    unittest.main()
