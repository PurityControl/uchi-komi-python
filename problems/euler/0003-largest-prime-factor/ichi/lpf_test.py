# -*- coding: utf-8 -*-

import unittest

import lpf

class LargestPrimeFactorTests(unittest.TestCase):

    def test_lpf_for_euler(self):
        self.assertEqual(
            6857,
            lpf.largest_prime_factor(600851475143)
        )

if __name__ == '__main__':
    unittest.main()
