import math, random

"""This is how you know I just read the Wikipedia article on monte carlo simulations
there's probably a one-line list comprehension way to do this but this is supposed
to help demonstrate the principles of Monte Carlo methods"""

N = 1000000  # Number of dots
hits = 0

for dot in range(N):
    x, y = random.random(), random.random()  # how random is random right?
    if (x ** 2 + y ** 2) <= 1:
        hits += 1.

fraction = hits / N

print("Calculated value of PI is:\t {}".format(4 * fraction))
print("math.pi value of PI is:\t\t {}".format(math.pi))
