
l = [i for i in xrange(1, 9999999)]     # Could use a generator instead but heh, good enough for now.


def getres(li):
    res = [1]   # Start from middle-out
    separation = 1  # seperation between diagonal numbers in the sequence (will also provide the width/height of grid)
    while separation < 1001:
        try:
            for j in range(4):  # Each "layer" in the spiral has foun numbers on the diagonals
                res.append(li[li.index(res[-1]) + separation + 1])
            separation += 2     # Seperation increases by 2 each layer
        except IndexError:
            break
    print "Sum : {}".format(sum(res))

getres(l)
