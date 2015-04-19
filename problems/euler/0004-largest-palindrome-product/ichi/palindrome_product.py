def palindrome_p(num):
    return str(num) == str(num)[::-1]


def max_palindrome_product(start, end):
    return max(x*y for x in range (start, end + 1)
                   for y in range (start, end + 1)
                   if palindrome_p(x*y))

