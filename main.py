def middleEndian(n):
    '''Returns the middle endian format of the number 'n' as an integer.'''
    '''A Middle-Endian Bit-Ordered number is defined by concatenating the middle bit of a bit with an odd number of bits, the bit before the middle, then the bit after the middle, then the bit before the bit before the middle, then the bit after the bit after the middle, etc, until the whole number has been rearranged. With an even number of bits, there are "two" middle bits, so start with the leftmost middle bit, then attach the rightmost middle bit, then the bit before the leftmost middle bit, etc, until all of the bits have been added, where the leftmost middle bit of the original number is the leftmost bit of the new number and the rightmost bit of the original number is still the rightmost bit of the middle-endian bit-ordered number.'''
    a = bin(n)[2:]
    temp = ""
    spread = 0
    i = len(a) / 2

    if len(a) == 2:
        return int(a, 2)

    #print "num %s" % n
    if len(a) % 2 == 1:
        temp += a[i]
        spread += 2
        i -= 1
        while (i >= 0):
            temp += a[i]
            temp += a[i+spread]
            spread += 2
            i -= 1
            #print a, temp, i, spread
    else:
        i -= 1
        temp += a[i]
        temp += a[i+1]
        spread += 3
        i -= 1
        #print i
        while (i >= 0):
            #print i, spread
            temp += a[i]
            temp += a[i+spread]
            spread += 2
            i -= 1
            #print a, temp, i, spread

    return int(temp, 2)

#print [(bin(middleEndian(i))[2:], bin(i)[2:]) for i in range(1, 23)]
RANGE = 1000000
x= filter((lambda x: middleEndian(x) == x), range(1, RANGE))
print x
