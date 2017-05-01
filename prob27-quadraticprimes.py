primes = []
notprimes = []
def isPrime(n):
    if n == 1 or n in primes:
        return True
    for i in range(2, n/2+1):
        if n%i == 0:
            notprimes.append(n)
            return False
    primes.append(n)
    return True

r = 999
maxnp = 0
ma = 0
mb = 0
abprod = 0
for a in range(-r, r+1):
    if a%10 == 0:
        print a
    for b in range(-r, r+1):
        n = 0
        np = 0
        while True:
            q = (n*n) + (a*n) + b
            if q < 1:
                #print n, "pass"
                n += 1
                pass
            elif isPrime(q):
                #print q, "is prime"
                np += 1
                n += 1
            else:
                break
        if np > maxnp:
            maxnp = np
            ma, mb, abprod = a, b, a * b

print "max primes =", maxnp, "a =", ma, "b =", mb, abprod
