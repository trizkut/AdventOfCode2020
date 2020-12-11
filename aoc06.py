from collections import Counter
tempstr = ''
groupsarr = []
pplarr = []
nn = 0
for line in open('inputs/input06.txt', 'r'):
    nn += 1
    if line == '' or line == '\n':
        groupsarr.append(tempstr)
        pplarr.append(nn-1)
        tempstr = ''
        nn = 0
    tempstr += line.rstrip()
groupsarr.append(tempstr)
pplarr.append(nn)
count_part1 = 0
count_part2 = 0
for i in range(0, len(groupsarr)):
    part1 = []
    part2 = []
    carr = Counter(groupsarr[i])
    for x in groupsarr[i]:
        if x not in part1:
            part1.append(x)
            if carr[x] == pplarr[i]:
                part2.append(x)
    count_part1 += len(part1)
    count_part2 += len(part2)

print(' Part 1: ', count_part1, '\n', 'Part 2: ', count_part2)
