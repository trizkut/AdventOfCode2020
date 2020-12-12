
pos = 0+0j
dir = 1+0j # East


rules = {
    'N': 1j,
    'E':  1,
    'W': -1,
    'S': -1j,
    'F': dir
}



for line in open('inputs/input12.txt', 'r'):
    ch, n = line[0], int(line[1:].strip())

    if (ch == 'L'):
        rules['F'] *= pow(1j, n // 90)
    elif (ch == 'R'):
        rules['F'] /= pow(1j, n // 90)
    else:
        pos += rules[ch] * n

print(int(abs(pos.real) + abs(pos.imag)))

