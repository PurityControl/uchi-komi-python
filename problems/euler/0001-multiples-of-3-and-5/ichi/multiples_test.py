# -*- coding: utf-8 -*-

import unittest

import multiples

class MultiplesTests(unittest.TestCase):

    def test_natural_numbers_to_10(self):
        self.assertEqual(
            23,
            multiples.to(10)
        )

    def test_natural_numbers_to_1000(self):
        self.assertEqual(
            233168,
            multiples.to(1000)
        )

if __name__ == '__main__':
    unittest.main()
