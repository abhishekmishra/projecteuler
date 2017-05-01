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
        for j = i**2, i**2+i, i**2+2i, i**2+3i, ..., not exceeding n :
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

def findNthPrime(n):
    """
    Based on prime number theorem
    pi(n) ~ n/log(n)
    
    https://primes.utm.edu/howmany.html
    http://en.wikipedia.org/wiki/Prime_number_theorem

    """
    # m is the number till which we will search
    m = int(2 * n * math.log(n))
    print "search for prime#", n, " till ", m
    p = findPrimes(m)

    if len(p) >= n:
        print "prime #", n, "is", p[n-1]
        return p[n-1]

    return None

print findNthPrime(5)
print findNthPrime(6)

print findNthPrime(10001)
