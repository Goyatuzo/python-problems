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

    def test_twenty_mins_to_hour(self):
        self.assertEqual('twenty minutes to six', timeInWords(5, 40))

    def test_twenty_four_to_hour(self):
        self.assertEqual('twenty four minutes to six', timeInWords(5, 36))

    def test_twenty_plus_past_hour(self):
        self.assertEqual('twenty eight minutes past five', timeInWords(5, 28))

    def test_minutes_past_hour(self):
        self.assertEqual('ten minutes past five', timeInWords(5, 10))

    def test_quarter_past_hour(self):
        self.assertEqual('quarter past five', timeInWords(5, 15))

    def test_half_past_hour(self):
        self.assertEqual('half past five', timeInWords(5, 30))

if __name__ == '__main__':
    unittest.main()
