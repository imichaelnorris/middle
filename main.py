def middleEndian(n):
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
