def get(factor):
    return


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
