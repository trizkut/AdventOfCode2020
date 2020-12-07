import re



def checkbag(bag, contents):
    if 'shiny gold' in contents:
        return True
    outp = False
    for x in contents:
        if x == 'no other': break
        outp = outp or checkbag(x, bagDict[x])
    return outp

bagList = []
bagDict = {}
for line in open('inputs/input7.txt', 'r'):
    test1 = re.split(' contain ', line)
    test1[0] = test1[0].replace('bags', '').strip()
    test1[1] = test1[1].replace('.', '')
    test1[1] = test1[1].replace(',', '')
    test1[1] = test1[1].replace('bags', '')
    test1[1] = test1[1].replace('bag', '')
    test2 = re.split('\d', test1[1])
    toBagList = []
    for x in test2:
        if (len(x) >= 3):
            toBagList.append(x.strip())
    bagList.append(toBagList)
    bagDict[test1[0]] = toBagList


keys = bagDict.keys()
count = 0
for key in keys:
    tmp = checkbag(key, bagDict[key])
    if (tmp): count += 1

print(count)

