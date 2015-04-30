# -*- coding: utf-8 -*-

import unittest

import primes

class PrimesTests(unittest.TestCase):

    def test_prime_at_6(self):
        self.assertEqual(
            13,
            primes.prime_at(6)
        )

    def test_primes_for_euler(self):
        self.assertEqual(
            104743,
            primes.prime_at(10001)
        )

if __name__ == '__main__':
    unittest.main()
