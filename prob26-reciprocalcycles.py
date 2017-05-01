from decimal import *
print getcontext()

rec = {}
for i in range(1, 10):
    r = Decimal(1) / Decimal(i)
    rec[i, r]

for i in rec:
    
