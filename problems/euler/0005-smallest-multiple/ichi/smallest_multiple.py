def smallest_multiple(limit):
    def _multiple_p(product, divisor):
        return product % divisor == 0

    divisors = range(1, limit)
    for product in product_series(limit):
        if all(_multiple_p(product, divisor) for divisor in divisors):
            return product

def product_series(product):
    """generator expression returning infinite list of multiples of product"""
    increment = product
    while True:
        yield product
        product += increment

