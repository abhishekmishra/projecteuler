# -*- coding: utf-8 -*-
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
        for j = i**2, i**2+i, i**2+2i, i**2+3i, ..., not exceeding sqrt(n):
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

# to get at least 500 primes
#m = int(2 * 500 * math.log(500))
p = findPrimes(1000)
print p

def triangleNumber(n):
    return (n * (n + 1))/2

def numFactors(n):
    nf = 1
    pf = {}
    for i in xrange(len(p)):
        if p[i] > n:
            break
        np = p[i]
        count = 1
        while np <= n and n%np == 0:
            pf[p[i]] = count
            count += 1
            np = p[i] ** count
        nf *= count
    return nf, pf


i = 1
while True:
    tn = triangleNumber(i)
    nf, pf = numFactors(tn)
    if i < 11 or i%10000 == 0:
        print i, tn, nf
    if nf >= 500:
        print tn, nf, pf
        break
    i+=1

# had to google the answer for this one... code had a bug but now works fine.
