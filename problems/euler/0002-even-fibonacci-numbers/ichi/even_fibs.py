def to(limit):
    def fibs_to(number):
        fibs = []
        a,b = 1, 2
        while a < number:
            fibs.append(a)
            a,b = b, a + b
        return fibs

    return sum([fib for fib in fibs_to(limit) if fib % 2 == 0])

