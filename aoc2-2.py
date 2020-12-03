import re

count = 0
for line in open('input2.txt', 'r'):
    test = re.split('[- :\n]', line) # n1 n2 key '' str ''
    if ( (int(test[0]) < 0) or (int(test[1]) < 0) or (int(test[0]) >= len(test[4])) or (int(test[1]) > len(test[4])) ):
        continue
    if (test[4][int(test[0])-1] == test[2]) != (test[4][int(test[1])-1] == test[2]):
        count += 1
print(count)
