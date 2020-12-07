sloperight = 1
slopedown = 2

inArr = []
lines = 0
for line in open('inputs/input3.txt', 'r'):
    inArr.append(line.rstrip())
    lines += 1
print(lines)

x = sloperight
y = slopedown

looplen = len(inArr[0])

trees = 1 if (inArr[0][0] == '#') else 0
while (y < lines):
    #print(x,y)
    if (inArr[y][x] == '#'):
        trees += 1
    x = (x + sloperight) % looplen
    y = (y + slopedown)

print(trees)