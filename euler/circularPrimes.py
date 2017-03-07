from quadraticPrime import isprime

# Circular prime problem


def iscircular(n):
    s = str(n)
    if len(s) == 1:
        return True     # single digit primes are all circular
    else:
        current = s
        for k in range(len(s)):
            current = current[1:] + current[:1]
            if not isprime(int(current)):
                return False
        return True
number = 0
for i in xrange(1, 1000000):
    if not isprime(i):
        continue
    else:
        if iscircular(i):
            number += 1

print number
