import math
import time

# Solves problem No. 12 (Highly divisible triangle number) of project euler


# Returns number of divisors
def get_divs(n):
    divs = 0
    for k in range(1, int(math.sqrt(n) + 1)):
        if n % k == 0:
            divs += 2
    return divs

iterator = 1
current = 0
starttime = time.time()
while get_divs(current) < 500:
    current += iterator
    iterator += 1
print current
print "Timing is: {}".format(time.time() - starttime)
