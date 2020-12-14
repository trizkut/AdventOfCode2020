import re
lines = []
mem = {}
def binary_to_decimal(binary):
    decimal = 0
    binary = binary[::-1]      #reverse the list
    power = 0   #declare power variable (for 1st elem == 0)
    for number in binary:
        if number == '1':
            decimal += 2**power
        power += 1 #increase power by 1
    return decimal

def permute_strings(inList):
    if (len(inList) == 1):
        return ['1', '0']
    else:
        outlist = []
        tmpoutList = permute_strings(inList[1:])
        for tmpstr in tmpoutList:
            if tmpstr != None:
                outlist.append('1' + tmpstr)
                outlist.append('0' + tmpstr)

        return outlist


index = 0
masks = {}
for line in open("inputs/input14.txt", 'r'):
    if (line[0:4] == 'mask'):
        masks[str(index)] = list(line.split(" = ")[1])
        lines.append("")
        index += 1
        continue
    index += 1
    lines.append(line.strip())
print(lines)

mask = ""
for i in range(0, len(lines)):
    if lines[i] == "":
        mask = masks[str(i)]
        continue
    print(lines[i])
    val = int(lines[i].split(" = ")[-1])
    ind = 0
    for j in range(0, len(lines[i])):
        if (lines[i][j] == ']'):
            ind = j
            break

    addr = int(lines[i][4:ind])
    binstr = format(addr, 'b')
    addrstr = list(binstr.zfill(36))
    numfloat = 0
    floats = []
    for j in range(0, len(mask)):
        if (mask[j] == '1'):
            addrstr[j] = mask[j]
        elif (mask[j] == 'X'):
            addrstr[j] = 'X'
            numfloat += 1
            floats.append(j)

    permutations = permute_strings(list(''.zfill(len(floats))))
    print("permutations: ", permutations)

    print(addrstr)
    for nn in range(0, len(permutations)):
        for pp in range(0,len(floats)):
            addrstr[floats[pp]] = permutations[nn][pp]

        #print(addrstr)
        newaddr = format(binary_to_decimal(addrstr), 'd')
        #print(newaddr)
        mem[str(newaddr)] = val

    print(addrstr)


    #newval = format(binary_to_decimal(addrstr), 'd')
    #print("oldval: ", val, "newval: ", newval)
    #mem[addr] = int(newval)

sum = 0
for memo in mem:
    sum+= mem[memo]

print("Sum: ", sum)




