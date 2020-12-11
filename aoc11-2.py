def find_chair(map, x, y, dx, dy):
    x += dx
    y += dy
    out = 0
    while (x < len(map[0]) and y < len(map) and y >= 0 and x >= 0):

        if map[y][x] == '#':
            out = 1
            break
        if map[y][x] == 'L':
            break


        x += dx
        y += dy
    return out




seatingMap = []
for line in open('inputs/input11.txt', 'r'):
    seatingMap.append(list(line.strip()))
changes = 1
newboard = []
for j in range(0, len(seatingMap)):
    newboard.append(seatingMap[j].copy())
while (changes != 0):

    changes = 0
    adj = []
    for i in range(0, len(seatingMap[0])):
        for j in range(0, len(seatingMap)):
            chaircount = 0
            if (i == 0 and j == 0):
                chaircount += find_chair(seatingMap, i, j, 0, 1)
                chaircount += find_chair(seatingMap, i, j, 1, 1)
                chaircount += find_chair(seatingMap, i, j, 1, 0)
            elif (i == 0 and j == len(seatingMap)-1):
                chaircount += find_chair(seatingMap, i, j, 0, -1)
                chaircount += find_chair(seatingMap, i, j, 1, -1)
                chaircount += find_chair(seatingMap, i, j, 1, 0)
            elif (i == len(seatingMap[0])-1 and j == 0):
                chaircount += find_chair(seatingMap, i, j, -1, 0)
                chaircount += find_chair(seatingMap, i, j, 0, 1)
                chaircount += find_chair(seatingMap, i, j, -1, 1)
            elif (i == len(seatingMap[0])-1 and j == len(seatingMap)-1):
                chaircount += find_chair(seatingMap, i, j, -1, 0)
                chaircount += find_chair(seatingMap, i, j, 0, -1)
                chaircount += find_chair(seatingMap, i, j, -1, -1)
            elif (i == 0):
                chaircount += find_chair(seatingMap, i, j, 0, -1)
                chaircount += find_chair(seatingMap, i, j, 0, 1)
                chaircount += find_chair(seatingMap, i, j, 1, -1)
                chaircount += find_chair(seatingMap, i, j, 1, 0)
                chaircount += find_chair(seatingMap, i, j, 1, 1)
            elif (j == 0):
                chaircount += find_chair(seatingMap, i, j, -1, 0)
                chaircount += find_chair(seatingMap, i, j, 1, 0)
                chaircount += find_chair(seatingMap, i, j, -1, 1)
                chaircount += find_chair(seatingMap, i, j, 0, 1)
                chaircount += find_chair(seatingMap, i, j, 1, 1)
            elif (i == len(seatingMap[0])-1):
                chaircount += find_chair(seatingMap, i, j, 0, -1)
                chaircount += find_chair(seatingMap, i, j, 0, 1)
                chaircount += find_chair(seatingMap, i, j, -1, -1)
                chaircount += find_chair(seatingMap, i, j, -1, 0)
                chaircount += find_chair(seatingMap, i, j, -1, 1)
            elif (j == len(seatingMap)-1):
                chaircount += find_chair(seatingMap, i, j, -1, 0)
                chaircount += find_chair(seatingMap, i, j, 1, 0)
                chaircount += find_chair(seatingMap, i, j, -1, -1)
                chaircount += find_chair(seatingMap, i, j, 0, -1)
                chaircount += find_chair(seatingMap, i, j, 1, -1)
            else:
                chaircount += find_chair(seatingMap, i, j, -1, -1)
                chaircount += find_chair(seatingMap, i, j, 0, -1)
                chaircount += find_chair(seatingMap, i, j, 1, -1)
                chaircount += find_chair(seatingMap, i, j, -1, 0)
                chaircount += find_chair(seatingMap, i, j, 1, 0)
                chaircount += find_chair(seatingMap, i, j, -1, 1)
                chaircount += find_chair(seatingMap, i, j, 0, 1)
                chaircount += find_chair(seatingMap, i, j, 1, 1)

            #print(adj, adj.count('#'), j, i, seatingMap[j][i])
            if (chaircount == 0 and seatingMap[j][i] == 'L'):
                newboard[j][i] = '#'
                changes += 1
            elif (chaircount >= 5 and seatingMap[j][i] == '#'):
                newboard[j][i] = 'L'
                changes += 1
            adj = []
    for j in range(0, len(seatingMap)):
        seatingMap[j] = newboard[j].copy()


print(seatingMap)
print(newboard)
count = 0
for j in range(0, len(seatingMap)):
    count += seatingMap[j].count('#')

print(count)

