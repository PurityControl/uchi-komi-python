def prime_at(position):
    """ returns the nth prime number

    args:
      position: the nth numbered prime
    """
    primes_list = list(take(position, primes()))
    return primes_list[-1]


def take(num, seq):
    """Generator takes num items from seq

    Args:
      num: number of items to take from list

      seq: the sequence to iterate over
    """
    counter = 1
    for item in seq:
        if counter <= num:
            yield item
        else:
            return
        counter += 1

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
