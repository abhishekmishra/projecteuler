# data is in p022_names.txt
def readNames():
    f = open('p022_names.txt', 'r')
    names = f.read().replace('"', '').split(',')
    names.sort()
    f.close()
    return names

names = readNames()

def charVal(c):
    v = ord(c) - ord('A') + 1
    return v

print charVal('B')

def nameScore(s):
    score = 0
    for c in s:
        score += charVal(c)
    return (names.index(s)+1) * score

print nameScore('COLIN')

sumScore = 0
for n in names:
    sumScore += nameScore(n)

print "Sum of name scores =", sumScore
