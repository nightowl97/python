import math

dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'fourty', 50:'fifty',
        60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 1000: 'thousand'}


def getlessthanhundred(i):
    if i <= 20 or (i < 100 and i % 10 == 0):
        return dict[i]
    elif i < 100:
        return dict[(i / 10) * 10] + dict[i % 10]    # Return length of 10s and unit


def gethundreds(i):
    return dict[i / 100] + 'hundred'


def getlen(k):
    if k == 1000:
        print 'onethousand'
        return len('onethousand')
    if k < 100:
        print getlessthanhundred(k)
        return len(getlessthanhundred(k))
    elif k % 100 == 0:
        print gethundreds(k)
        return len(gethundreds(k))
    else:
        print gethundreds(k) + 'and' + getlessthanhundred(k % 100)
        return len(gethundreds(k)) + len('and') + len(getlessthanhundred(k % 100))


total = 0
for i in range(1, 1001):
    total += getlen(i)
print total
