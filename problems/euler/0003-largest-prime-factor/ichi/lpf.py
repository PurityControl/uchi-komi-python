def largest_prime_factor(dividend):
    """ given a dividend, finds all the prime factors for it
    and returns the largest of the prime factors

    args:
      dividend: the number you want to calculate the largest
      prime factor for
    """
    factors = []
    while product_of_factors(factors) < dividend:
        factors.append(
          lowest_prime_factor(reduced_dividend(dividend, factors)))
    return max(factors)


def reduced_dividend(dividend, factors):
    """The new dividend as a result of dividing the original
    dividend by the list of prime factors calculated so far."""
    return dividend/product_of_factors(factors)


def product_of_factors(seq):
    """return the product of numbers in the list or 1 for the
    empty list to prevent division by zero errors"""
    return reduce(lambda x, y: x*y, seq, 1)


def lowest_prime_factor(factor):
    for prime in primes():
        if factor_p(factor, prime):
            return prime


def factor_p(factor, divisor):
    return factor % divisor == 0


def get_kval_primes(k_val, primes):
    #filter primes only from 1+kval and 1-kval
    return [x for x in [k_val*6-1, k_val*6+1] if  prime_p(x, primes)]


def prime_p(num, primes):
    #filter primes smaller than num and see if they are factors
    for prime in primes:
        if num % prime == 0:
            return False
    return True

def at_end_of_primes(counter, primes):
    return counter == len(primes) - 1


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
    counter = 0
    primes = [2, 3]
    k_val = 1
    while True:
        while at_end_of_primes(counter, primes):
            next_primes = get_kval_primes(k_val, list(primes))
            k_val += 1
            for prime in next_primes:
                primes.append(prime)
        yield primes[counter]
        counter += 1
