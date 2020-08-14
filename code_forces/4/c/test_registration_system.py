import unittest

from registration_system import registration_system as foo

# The dictionary is stored across the three test cases
class TestRegistrationSystem(unittest.TestCase):
    def test_given(self):
        self.assertEqual('OK', foo('abacaba'))
        self.assertEqual('OK', foo('acaba'))
        self.assertEqual('abacaba1', foo('abacaba'))
        self.assertEqual('OK', foo('acab'))
    
    def test_given_two(self):
        self.assertEqual('OK', foo('first'))
        self.assertEqual('first1', foo('first'))
        self.assertEqual('OK', foo('second'))
        self.assertEqual('second1', foo('second'))
        self.assertEqual('OK', foo('third'))
        self.assertEqual('third1', foo('third'))
    
    def test_self(self):
        self.assertEqual('OK', foo('testing'))
        self.assertEqual('testing1', foo('testing'))
        self.assertEqual('testing2', foo('testing'))

if __name__ == '__main__':
    unittest.main()