# -*- coding: utf-8 -*-

import unittest

import palindrome_product

class PalindromeProductTests(unittest.TestCase):

    def test_palindrome_product_for_euler(self):
        self.assertEqual(
            906609,
            palindrome_product.max_palindrome_product(100, 999)
        )

if __name__ == '__main__':
    unittest.main()
