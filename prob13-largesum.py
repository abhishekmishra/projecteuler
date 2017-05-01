#input data is in prob13-data.txt
#REVISIT since this is trivial in python, how would you do it with limited precision
n = []
f = open("prob13-data.txt")
for l in f:
    n.append(int(l))
f.close()

sum = 0
for i in n:
    sum += i

print sum


