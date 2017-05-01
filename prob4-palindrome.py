def is_palindrome(n):
    sn = str(n)
    for i in range(len(sn)/2 + 1):
        if sn[i] != sn[-i-1]:
            return False
    return True

print is_palindrome(9009)
print is_palindrome(90109)

max = 0
for i in range(100,1000):
    for j in range(i,1000):
        p = i * j
        if p > max and is_palindrome(p):
            max = p

print max
    
