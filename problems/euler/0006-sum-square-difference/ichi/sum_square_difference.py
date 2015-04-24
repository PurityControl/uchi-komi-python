def difference(limit):
    return _square_sums(limit) - _sum_squares(limit)

def _sum_squares(limit):
    return sum([x*x for x in range(1, 1 + limit)])

def _square_sums(limit):
    return pow(sum([x for x in range(1, 1 + limit)]),2)
