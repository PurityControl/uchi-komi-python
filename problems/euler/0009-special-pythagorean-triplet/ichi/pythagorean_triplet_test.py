# -*- coding: utf-8 -*-

import unittest

import pythagorean_triplet

class PythagoreanTripletTests(unittest.TestCase):

    def test_euler_pythagorean_triplet(self):
        self.assertEqual(
            31875000,
            pythagorean_triplet.pythagorean_triplet(1000)
        )

if __name__ == '__main__':
    unittest.main()
