def numDigits(n):
    return len(str(n))

def findFibonacciWith1000Digits():
    prev = 1
    fib = 1
    n = 2
    while numDigits(fib) != 1000:
        fib, prev = fib + prev, fib
        n += 1
        #print numDigits(fib)
    print fib, n

findFibonacciWith1000Digits()
