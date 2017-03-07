from quadraticPrime import isprime

# Truncatable primes problem

i = 10


def truncate(n, s):
    # From right
    if s == 'right':
        for j in range(len(str(n)) - 1):
            trunc1 = int(str(n)[:-(j + 1)])
            if not isprime(trunc1):
                return False
        return True
    # From left
    if s == 'left':
        for j in range(len(str(n)) - 1):
            trunc2 = int(str(n)[j + 1:])
            if not isprime(trunc2):
                return False
        return True
    else:
        raise TypeError

li = []
while True:
    i += 1
    if len(li) > 10:
        break
    if not isprime(i):
        continue
    if not (truncate(i, 'left') and truncate(i, 'right')):
        continue
    print i
    li.append(i)

print li
