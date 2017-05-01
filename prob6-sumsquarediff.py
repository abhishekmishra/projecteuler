# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# (a + b + c) ** 2 = a **2 + b ** 2 + c **2 + 2ab + 2ac + 2bc
# minus a ** 2 + b ** 2 + c ** 2
# equals 2 (ab + ac + bc)
#
# Twice sum of products of all possible pairs

def distinctPairs(n):
    pairs = []
    for i in range(1,n+1):
        for j in range(i+1, n+1):
            pairs.append((i, j))
    return pairs

print distinctPairs(3)

def diff(n):
    pairs = distinctPairs(n)
    sum = 0
    for p in pairs:
        sum = sum + (p[0] * p[1])
    return 2 * sum

print diff(10)
print diff(100)

#TODO complete with better solution
#REVISIT 
