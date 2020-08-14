import unittest

from way_too_long_words import way_too_long_words as foo

class TestWayTooLongWords(unittest.TestCase):
    def test_given(self):
        self.assertEqual('word', foo('word'))
        self.assertEqual('l10n', foo('localization'))
        self.assertEqual('i18n', foo('internationalization'))
        self.assertEqual('p43s', foo('pneumonoultramicroscopicsilicovolcanoconiosis'))

if __name__ == '__main__':
    unittest.main()
