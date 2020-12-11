
instrList = []

for line in open('inputs/input08.txt', 'r'):
    instr = line.strip().split(" ")
    instrList.append(instr)




for i in range(0, len(instrList)):

    accumulator = 0
    index = 0
    dupe = 0
    executedList = [False] * len(instrList)

    while (index < len(instrList)):
        curInstr = instrList[index][0]
        if (index == i):
            if (curInstr == 'nop'): curInstr = 'jmp'
            if (curInstr == 'jmp'): curInstr = 'nop'
        if (executedList[index]):
            print('Duplicate Execution, Terminating;  Accumulator Value: ', accumulator)
            dupe = 1
            break
        executedList[index] = True
        if (curInstr == 'nop'):
            index += 1
            continue
        if (curInstr == 'acc'):
            accumulator += int(instrList[index][1])
        if (curInstr == 'jmp'):
            index += int(instrList[index][1])
        else:
            index += 1

    if (not dupe): #if no duplicate execution after loop, this is the right instruction to replace
        print('Successful execution; Accumulator value: ', accumulator)
        break
