# Write a program which will find all such numbers which are divisible by 7 but
# are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# Hints:
# Consider use range(#begin, #end) method

import math

list = []
for x in xrange(2000,3201):
    if math.fmod(x,7) == 0:
        if not math.fmod(x,5) == 0:
            #print "Values are: %d" %x
            list.append(x)
print list
