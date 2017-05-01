def getFactors(n):
    factors = []
    for i in range(1, n/2+1):
        if n%i == 0:
            factors.append(i)
    return factors, sum(factors)

def findAbundantNumbers(n):
    abundants = {}
    for i in range(n+1):
        factors, sumfactors = getFactors(i)
        if i < sumfactors:
            abundants[i] = sumfactors
    return abundants

print findAbundantNumbers(100)

abundants = findAbundantNumbers(28123)

cannotBeSummed = []
for i in range(1, 28123):
    cs = False
    for a in abundants:
        if a < i and i - a in abundants:
            cs = True
            break
    if not cs:
        cannotBeSummed.append(i)

print cannotBeSummed, sum(cannotBeSummed)
