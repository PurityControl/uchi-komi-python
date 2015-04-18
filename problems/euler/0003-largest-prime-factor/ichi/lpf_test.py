# -*- coding: utf-8 -*-

import unittest

import lpf

class LargestPrimeFactorTests(unittest.TestCase):

    def test_even_fibs_to_4000000(self):
        self.assertEqual(
            6857,
            lpf.largest_prime_factor(600851475143)
        )

if __name__ == '__main__':
    unittest.main()
