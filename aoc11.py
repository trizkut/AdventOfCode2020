
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
            #print(j, i)
            #print(len(seatingMap), len(seatingMap[0]))
            if (i == 0 and j == 0):
                adj.append(seatingMap[j+1][i])
                adj.append(seatingMap[j+1][i+1])
                adj.append(seatingMap[j][i+1])
            elif (i == 0 and j == len(seatingMap)-1):
                adj.append(seatingMap[-2][i])
                adj.append(seatingMap[-2][i+1])
                adj.append(seatingMap[-1][i+1])
            elif (i == len(seatingMap[0])-1 and j == 0):
                adj.append(seatingMap[j][-2])
                adj.append(seatingMap[j+1][-1])
                adj.append(seatingMap[j+1][-2])
            elif (i == len(seatingMap[0])-1 and j == len(seatingMap)-1):
                adj.append(seatingMap[-2][-1])
                adj.append(seatingMap[-1][-2])
                adj.append(seatingMap[-2][-2])
            elif (i == 0):
                adj.append(seatingMap[j-1][i])
                adj.append(seatingMap[j+1][i])
                adj.append(seatingMap[j-1][i+1])
                adj.append(seatingMap[j][i+1])
                adj.append(seatingMap[j+1][i+1])
            elif (j == 0):
                adj.append(seatingMap[j][i-1])
                adj.append(seatingMap[j][i+1])
                adj.append(seatingMap[j+1][i-1])
                adj.append(seatingMap[j+1][i])
                adj.append(seatingMap[j+1][i+1])
            elif (i == len(seatingMap[0])-1):
                adj.append(seatingMap[j-1][i])
                adj.append(seatingMap[j+1][i])
                adj.append(seatingMap[j-1][i-1])
                adj.append(seatingMap[j][i-1])
                adj.append(seatingMap[j+1][i-1])
            elif (j == len(seatingMap)-1):
                adj.append(seatingMap[j][i-1])
                adj.append(seatingMap[j][i+1])
                adj.append(seatingMap[j-1][i-1])
                adj.append(seatingMap[j-1][i])
                adj.append(seatingMap[j-1][i+1])
            else:
                adj.append(seatingMap[j-1][i-1])
                adj.append(seatingMap[j-1][i])
                adj.append(seatingMap[j-1][i+1])
                adj.append(seatingMap[j][i-1])
                adj.append(seatingMap[j][i+1])
                adj.append(seatingMap[j+1][i-1])
                adj.append(seatingMap[j+1][i])
                adj.append(seatingMap[j+1][i+1])

            #print(adj, adj.count('#'), j, i, seatingMap[j][i])
            if (adj.count('#') == 0 and seatingMap[j][i] == 'L'):
                newboard[j][i] = '#'
                changes += 1
            elif (adj.count('#') >= 4 and seatingMap[j][i] == '#'):
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
