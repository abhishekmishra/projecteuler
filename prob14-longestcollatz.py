def countCollatz(n):
    orig = n
    count = 1
    while n > 1:
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        count += 1
    #print "collatz chain count of ", orig, "=", count
    return count


max = 0
loc = 0
for i in range(999999, 0, -1):
    cc = countCollatz(i)
    if cc > max:
        print "collatz chain count of ", i, "=", cc
        max = cc
        loc = i

print max, loc
