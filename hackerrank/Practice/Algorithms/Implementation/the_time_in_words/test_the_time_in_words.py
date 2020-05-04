import unittest

from the_time_in_words import timeInWords

class TestTheTimeInWords(unittest.TestCase):
    def test_given_1(self):
        self.assertEqual('thirteen minutes to six', timeInWords(5, 47))

    def test_given_2(self):
        self.assertEqual('three o\' clock', timeInWords(3, 0))

    def test_given_3(self):
        self.assertEqual('quarter past seven', timeInWords(7, 15))

    def test_keyword_to_hour(self):
        self.assertEqual('quarter to six', timeInWords(5, 45))

if __name__ == '__main__':
    unittest.main()
