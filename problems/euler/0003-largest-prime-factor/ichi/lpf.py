def largest_prime_factor(dividend):
    """ given a dividend, finds all the prime factors for it
    and returns the largest of the prime factors

    args:
      dividend: the number you want to calculate the largest
      prime factor for
    """
    factors = []
    while _product_of_factors(factors) < dividend:
        factors.append(
          _lowest_prime_factor(_reduced_dividend(dividend, factors)))
    return max(factors)


def _reduced_dividend(dividend, factors):
    """The new dividend as a result of dividing the original
    dividend by the list of prime factors calculated so far."""
    return dividend/_product_of_factors(factors)


def _product_of_factors(seq):
    """return the product of numbers in the list or 1 for the
    empty list to prevent division by zero errors"""
    return reduce(lambda x, y: x*y, seq, 1)


def _lowest_prime_factor(factor):
    for prime in primes():
        if _factor_p(factor, prime):
            return prime


def _factor_p(factor, divisor):
    return factor % divisor == 0


def up_to(num, seq):
    """Generator given num yields all items from the sequence until
    num is exceeded

    Args:
      num: number that represents a limit the generator will stop
      at when exceeded

      seq: the sequence to iterate over
    """
    for item in seq:
        if item <= num:
            yield item
        else:
            return

def primes():
    """ Geneartor that lazily evaluates the next prime number.

    Warning: This will produce an infinte sequence"""
    def _end_of_primes_p(counter, primes):
        return counter == len(primes) - 1

    def _prime_p(num, primes):
        for prime in primes:
            if num % prime == 0:
                return False
        return True


    def _get_kval_primes(k_val, primes):
        return [x for x in [k_val*6-1, k_val*6+1] if  _prime_p(x, primes)]


    counter = 0
    primes = [2, 3]
    k_val = 1
    while True:
        while _end_of_primes_p(counter, primes):
            next_primes = _get_kval_primes(k_val, list(primes))
            k_val += 1
            for prime in next_primes:
                primes.append(prime)
        yield primes[counter]
        counter += 1
