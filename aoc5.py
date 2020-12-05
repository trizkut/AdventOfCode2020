myList = []
seats = []
for line in open('input5.txt', 'r'):
    rowstr = line[0:7]
    colstr = line[7:len(line)]
    lower = 0
    upper = 128
    for i in range(0,7):
        if rowstr[i] == 'F':
            upper = upper - ((upper-lower)/2)
        elif rowstr[i] == 'B':
            lower = lower + ((upper-lower)/2)
    row = lower

    lower = 0
    upper = 8
    for i in range(0,3):
        if colstr[i] == 'L':
            upper = upper - ((upper-lower)/2)
        elif colstr[i] == 'R':
            lower = lower + ((upper-lower)/2)
    col = lower
    seats.append(row*8 + col)

seats.sort()
targetseat = seats[0]
for i in range(0,len(seats)-1):
    diff = seats[i+1] - seats[i]
    if diff >= 2:
        targetseat = (seats[i+1] + seats[i]) /2
        break
print(seats[len(seats)-1], targetseat)