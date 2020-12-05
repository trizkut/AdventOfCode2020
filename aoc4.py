import re
curPassport = []
validPassports = 0

def processPassport(pp):
    valpp = 0
    numf = 0
    print(pp)
    print(len(pp))
    for i in range(0, len(pp), 2):
        if (pp[i] == 'byr'):
            if ( (len(pp[i+1]) == 4) and (int(pp[i+1]) >= 1920) and (int(pp[i+1]) <= 2002) ):
                numf += 1
        elif (pp[i] == 'iyr'):
            if ( (len(pp[i+1]) == 4) and (int(pp[i+1]) >= 2010) and (int(pp[i+1]) <= 2020) ):
                numf += 1
        elif (pp[i] == 'eyr'):
            if ( (len(pp[i+1]) == 4) and (int(pp[i+1]) >= 2020) and (int(pp[i+1]) <= 2030) ):
                numf += 1
        elif (pp[i] == 'hgt'):
            strlen = len(pp[i+1])
            if strlen <= 2: continue
            nn = int(pp[i+1][0:strlen-2])
            if (not nn): continue
            if (pp[i+1][strlen-2:strlen] == 'cm'):
                if (nn >= 150 and nn <= 193):
                    numf += 1
            elif (pp[i+1][strlen-2:strlen] == 'in'):
                if (nn >= 59 and nn <= 76):
                    numf += 1
        elif (pp[i] == 'hcl'):
            if (pp[i+1][0] == '#' and len(pp[i+1]) == 7 and re.search('^[a-zA-Z0-9]+$', pp[i+1][1:len(pp[i+1])-1]) ):
                numf += 1
        elif (pp[i] == 'ecl'):
            if ( (pp[i+1] == 'amb')
                    or (pp[i+1] == 'blu')
                    or (pp[i+1] == 'brn')
                    or (pp[i+1] == 'gry')
                    or (pp[i+1] == 'grn')
                    or (pp[i+1] == 'hzl')
                    or (pp[i+1] == 'oth') ):
                numf += 1
        elif (pp[i] == 'pid'):
            if (len(pp[i+1]) == 9 and int(pp[i+1])):
                numf += 1
    print(numf)
    return numf



for line in open('input4.txt', 'r'):
    if (line == '\n'): # new passport, process old data
        valFields = processPassport(curPassport)
        if (valFields == 7): validPassports += 1
        curPassport = []
    else:
        curPassport += re.split('[: ]',line.rstrip())
    #print(curPassport)
    #print(line)
valFields = processPassport(curPassport)
if (valFields == 7): validPassports += 1

print(validPassports)