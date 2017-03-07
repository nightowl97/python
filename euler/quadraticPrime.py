# Interesting transformer's name by the way am I right?
# this one is for the 27th quadratic primes problem

from math import sqrt
from itertools import islice, count


def isprime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))

if __name__ == '__main__':
    m = 0   # maximum
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            # Current equation: n^(2) + a.n + b

            i = 0
            while True:
                if isprime((i ** 2) + (a * i) + b):
                    i += 1
                    continue
                elif i > m:
                    print "a: {}, b: {}".format(a, b)
                    m = i
                    break
                else: break
