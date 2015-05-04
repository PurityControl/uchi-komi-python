# -*- coding: utf-8 -*-

import unittest

import primes

class PrimesTests(unittest.TestCase):

    def test_prime_at_6(self):
        self.assertEqual(
            17,
            primes.sum_to(10)
        )

    def test_primes_for_euler(self):
        self.assertEqual(
            142913828922,
            primes.sum_to(2000000)
        )

if __name__ == '__main__':
    unittest.main()
