# -*- coding: utf-8 -*-
import math

def findProperDivisorsSum(n):
    d = 0
    for i in range(1, n/2+1):
        if n%i == 0:
            d += i
    return d

alld = {}
for i in range(1, 10001):
    alld[i] = findProperDivisorsSum(i)

sum_amic = 0
for k in alld:
    if alld[k] in alld and alld[k] != k and alld[alld[k]] == k:
        print k, "is amicable number"
        sum_amic += k

print "sum of amicabe numbers till 10000 is", sum_amic
