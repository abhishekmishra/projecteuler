#read data (stored in file prob11-data.txt)

grid = [[0 for x in range(20)] for x in range(20)]

f = open("prob11-data.txt")
row = 0
for l in f:
    col = 0
    for num in l.split(" "):
        grid[row][col] = int(num)
        col += 1
    row += 1
f.close()

print grid

def getN(i, j):
    if i < 0 or j < 0 or i > 19 or j > 19:
        return 0
    else:
        return grid[i][j]

m = 0
li = 0
lj = 0
for i in range(20):
    for j in range(20):
        diagup = getN(i, j) * getN(i-1, j-1) * getN(i-2, j-2) * getN(i-3, j-3)
        diagdown = getN(i, j) * getN(i+1, j+1) * getN(i+2, j+2) * getN(i+3, j+3)
        diagleft = getN(i, j) * getN(i+1, j-1) * getN(i+2, j-2) * getN(i+3, j-3)
        diagright = getN(i, j) * getN(i-1, j+1) * getN(i-2, j+2) * getN(i-3, j+3)
        up = getN(i, j) * getN(i-1, j) * getN(i-2, j) * getN(i-3, j)
        down = getN(i, j) * getN(i+1, j) * getN(i+2, j) * getN(i+3, j)
        left = getN(i, j) * getN(i, j-1) * getN(i, j-2) * getN(i, j-3)
        right = getN(i, j) * getN(i, j+1) * getN(i, j+2) * getN(i, j+3)

        mij = max(diagup, diagdown, diagleft, diagright, up, down, left, right)
        if mij > m:
            m = mij
            li = i
            lj = j
                   
print m, li, lj

