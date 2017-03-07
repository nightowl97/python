import time

# import data from files
with open("small.in") as f:
    lines = f.readlines()
    data = []
    firstline = lines[0].split(" ")
    rows = int(firstline[0])
    columns = int(firstline[1])
    minimum = int(firstline[2])
    maximum = int(firstline[3])
    for line in lines[1:]:
        data.append(list(line.strip()))


# Definitions ###############################

def getslice(((row1, row2), (col1, col2))):
    # Get Slice
    pslice = []
    for i in range(row1, row2 + 1):
        pslice.append(data[i][col1: col2 + 1])
    return pslice


# Check if slice is valid
def validate(((row1, row2), (col1, col2))):
    potentialslice = getslice(((row1, row2), (col1, col2)))
    # Validate
    tnum = 0
    mnum = 0
    for i in potentialslice:
        for j in i:
            if j == "T":
                tnum += 1
            elif j == "M":
                mnum += 1
            else:
                print "error"

    if tnum < minimum or mnum < minimum:
        return False
    if len(potentialslice) * len(potentialslice[0]) > maximum:
        return False
    return True


# Check if two slices overlap
def overlaps(slice1, slice2):
    if slice2[0][0] > slice1[0][1] or slice2[1][0] > slice1[1][1]:
        return False
    elif slice1[0][0] > slice2[0][1] or slice1[1][0] > slice2[1][1]:
        return False
    else:
        return True


# Get all possible valid slices
def bruteforce():
    slices = []
    for i in range(rows):
        for j in range(i, rows):
            if j - i > maximum:
                break
            for u in range(columns):
                for v in range(u, columns):
                    if v - u > maximum or (j - i + 1) * (u - v + 1) > maximum:
                        break
                    curr = ((i, j), (u, v))
                    if validate(curr):
                        slices.append(curr)
    print len(slices)
    return slices
    

# Construct configurations compatible with slice
def getsliceconfs(pslice):
    candidates = []
    # remove overlapping slices
    for s in bruteforce():
        if not overlaps(pslice, s):
            candidates.append(s)
    return len(candidates)


# Execution ###########################

starttime = time.time()
bruteforce()
print "in " + str(time.time() - starttime)

print "confs: " + str(getsliceconfs(((3, 4), (2, 5))))
