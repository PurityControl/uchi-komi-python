# -*- coding: utf-8 -*-

import unittest

import sum_square_difference

class SumSquareDifferenceTests(unittest.TestCase):

    def test_sum_square_difference_for_euler(self):
        self.assertEqual(
            25164150,
            sum_square_difference.difference(100)
        )

if __name__ == '__main__':
    unittest.main()
