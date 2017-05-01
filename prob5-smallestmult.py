# -*- coding: utf-8 -*-
# smallest positive number that is evenly divisible by all of the numbers from 1 to 20


# brute force
# start at 1*2^4*3^2*5*7*11*13*17*19 = 232792560
# all primes and their powers that occur at or before 20
n = 232792560
while True:
    div = True
    for i in range(1, 21):
        if n%i != 0:
            div = False
    if div:
        break
    n+=1
    if n%1000 == 0:
        print n

print n

# general algorithm based on overiview of the problem at website
import math

def findPrimes(n):
    """
    Based on sieve of eratosthenes
    pseudo code from http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    Input: an integer n > 1
 
    Let A be an array of Boolean values, indexed by integers 2 to n,
    initially all set to true.
 
     for i = 2, 3, 4, ..., not exceeding √n:
      if A[i] is true:
        for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n :
          A[j] := false
 
    Output: all i such that A[i] is true.

    """
    a = [True] * (n+1)
    for i in range(2, n+1):
        if a[i] == True:
            for j in range(i*i, n+1, i):
                a[j] = False
    primes = []
    for i in range(2, n+1):
        if a[i] == True:
            primes.append(i)
    return primes

print findPrimes(10)
print findPrimes(25)

def findMaxNumberDivisibleByAll(k):
    p = findPrimes(k)
    a = [int(0)] * len(p)
    n = 1
    i = 1
    check = True
    limit = math.sqrt(k)
    for i in range(0, len(p)):
        a[i] = 1
        if check:
            if p[i] <= limit:
                a[i] = math.floor(math.log(k)/math.log(p[i]))
            else:
                check = False
        n = int(n * (p[i] ** a[i]))
    return n

print findMaxNumberDivisibleByAll(20)
