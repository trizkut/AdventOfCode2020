preamble = []
data = []
preamble_length = 25
og_data = []
i = 0
for line in open('inputs/input09.txt', 'r'):
    if (i < preamble_length):
        preamble.append(int(line))
    else:
        data.append(int(line))
    og_data.append(int(line))
    i += 1

i = 0

notSumNumber = -1
while (i < len(data)):

    isSum = False
    for j in range(0, preamble_length):
        for k in range(1, preamble_length):
            if (preamble[j] + preamble[k] == data[i]):
                isSum = True
                del preamble[0]
                preamble.append(data[0])
                del data[0]

        if (isSum): break

    if (not isSum):
        notSumNumber = data[0]
        break
print("Rule-breaking number: ", notSumNumber)


# find contiguous set
for i in range(0, len(og_data)-1):
    sum = og_data[i]
    sumSet = [og_data[i]]
    foundSet = False

    for j in range(i+1, len(og_data)):
        sum += og_data[j]
        sumSet.append(og_data[j])
        if (sum > notSumNumber):
            break
        if (sum == notSumNumber):
            foundSet = True
            break

    if (foundSet):
        break

print("Min: ", min(sumSet), "Max: ", max(sumSet))
print("Sum of Min & Max: ", min(sumSet) + max(sumSet))