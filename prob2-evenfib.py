m = 0
n = 1
sum = 0
while True:
    temp = n
    n = n + m
    m = temp
    if n < 4000000:
        if n%2 == 0:
            sum += n
    else:
        break
print sum
        
