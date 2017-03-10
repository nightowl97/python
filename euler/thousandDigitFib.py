
# get index of first 1000-digit Fibonacci number

previous = 1
curr = 1
index = 2

while len(str(curr)) < 1000:
    index += 1
    nex = curr + previous
    previous = curr
    curr = nex
print index
