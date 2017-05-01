def factorial(n):
    p = 1
    for i in range(1, n+1):
        p *= i
    return p

def sumDigits(n):
    a = str(n)
    sum = 0
    for x in a:
        sum += int(x)
    return sum

print sumDigits(factorial(100))
