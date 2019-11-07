import unittest

import nth_prime

class TestNthPrime(unittest.TestCase):
    def test_get_primes(self):
        self.assertEqual([2], nth_prime.get_primes(2))
        self.assertEqual([2, 3], nth_prime.get_primes(3))
        self.assertEqual([2, 3, 5], nth_prime.get_primes(5))

    def test_given(self):
        self.assertEqual([5], nth_prime.get_nth_primes([3]))
        self.assertEqual([13], nth_prime.get_nth_primes([6]))
        self.assertEqual([5, 13], nth_prime.get_nth_primes([3, 6]))
        self.assertEqual([13, 5], nth_prime.get_nth_primes([6, 3]))

if __name__ == '__main__':
    unittest.main()