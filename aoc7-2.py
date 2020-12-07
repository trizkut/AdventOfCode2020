import re



def checkbag(bag, contents, countDict):
    outp = 1
    for x in range(0,len(contents)):
        if contents[x] == 'no other': break
        outp = outp + int(countDict[x])*checkbag(contents[x], bagDict[contents[x]], bagCountDict[contents[x]])
    return outp

bagList = []
bagDict = {}
bagCountDict = {}
for line in open('inputs/input7.txt', 'r'):
    test1 = re.split(' contain ', line)
    nums = re.findall('\d+', line)


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
    bagCountDict[test1[0]] = nums

print(checkbag('shiny gold', bagDict['shiny gold'], bagCountDict['shiny gold']) - 1) #subtract 1 to not count initial gold bag
