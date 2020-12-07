import re
count = 0
for line in open('inputs/input2.txt', 'r'):
    test = re.split('[- :\n]', line) # n1 n2 key '' str ''
    asdf = test[4].count(test[2])
    if ( (asdf >= int(test[0]) ) and ( asdf <= int(test[1]) ) ):
        count += 1
print(count)