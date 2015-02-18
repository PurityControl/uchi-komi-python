# -*- coding: utf-8 -*-

import unittest

import even_fibs

class EvenFibsTests(unittest.TestCase):

    def test_even_fibs_to_4000000(self):
        self.assertEqual(
            4613732,
            even_fibs.to(4000000)
        )

if __name__ == '__main__':
    unittest.main()
