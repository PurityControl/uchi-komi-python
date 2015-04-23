# -*- coding: utf-8 -*-

import unittest

import smallest_multiple

class SmallestMultipleTests(unittest.TestCase):

    def test_smallest_product_for_euler(self):
        self.assertEqual(
            232792560,
            smallest_multiple.smallest_multiple(20)
        )

if __name__ == '__main__':
    unittest.main()
