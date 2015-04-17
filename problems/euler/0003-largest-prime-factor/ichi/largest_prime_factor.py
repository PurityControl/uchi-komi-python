def get(factor):
    return max(x for x in up_to(factor, primes()) if factor_p(factor,x))


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
