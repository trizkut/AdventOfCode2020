#key: N, E are positive
#     S, W are negative


pos = 0j
waypoint = 10 + 1j

directions = {'N': 1j,
              'E': 1,
              "S": -1j,
              "W": -1}


for line in open('inputs/input12.txt', 'r'):

    c, n = line[0], int(line[1:].strip())
    if (c == 'L'):
        waypoint *= pow(1j, (n // 90))
    elif (c == 'R'):
        waypoint /= pow(1j, (n // 90))
    elif (c == 'F'):
        pos += (waypoint) * n
    else:
        waypoint += n * directions[c]

print(pos)
print(int(abs(pos.real) + abs(pos.imag)))