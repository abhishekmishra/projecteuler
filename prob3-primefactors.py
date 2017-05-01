def isprime(i):
    j = 2
    while j < i:
        if i%j == 0:
            return False
        j = j + 1
    return True

# largest prime factor of 600851475143
n = 600851475143
max = 0
i = 2
while i <= n:
    if n%i == 0:
        if isprime(i):
            max = i
            n = n/i
            print "new n = ", n
    if i%100000 == 0:
        print i
    i = i + 1
    
print max
