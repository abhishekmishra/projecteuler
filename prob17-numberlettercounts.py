baseWords = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand"
    }
    
def numberToLetters(n):
    if n < 21:
        return baseWords[n]
    elif n < 100:
        if n%10 == 0:
            return baseWords[n-(n%10)]
        else:
            return baseWords[n-(n%10)] + "-" + numberToLetters(n%10)
    elif n < 1000:
        f = n - (n%100)
        if n%100 == 0:
            return baseWords[f/100] + "-" + baseWords[100]
        else:
            return baseWords[f/100] + "-" + baseWords[100] + " and " + numberToLetters(n%100)
    elif n==1000:
        return baseWords[1] + " " + baseWords[n]

print numberToLetters(12)    
print numberToLetters(252)
print numberToLetters(250)
print numberToLetters(200)
print numberToLetters(207)
print numberToLetters(212)
print numberToLetters(76)
print numberToLetters(342)
print numberToLetters(115)

s = ""
for i in range(1, 1001):
    x = numberToLetters(i)
    print x
    s += x.replace(" ", "").replace("-", "")

#print s
print len(s)

