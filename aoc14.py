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

    addr = lines[i][4:ind]
    binstr = format(val, 'b')
    valstr = list(binstr.zfill(36))
    for j in range(0, len(mask)):
        if (mask[j] == '1' or mask[j] == '0'):
            valstr[j] = mask[j]

    print(valstr)

    newval = format(binary_to_decimal(valstr), 'd')
    print("oldval: ", val, "newval: ", newval)
    mem[addr] = int(newval)

sum = 0
for memo in mem:
    sum+= mem[memo]

print("Sum: ", sum)
