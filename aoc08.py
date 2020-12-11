accumulator = 0
index = 0
instrList = []

for line in open('inputs/input08.txt', 'r'):
    instr = line.strip().split(" ")
    instrList.append(instr)

executedList = [False] * len(instrList)


while (index < len(instrList)):

    if (executedList[index]):
        print('Duplicate Execution, Terminating;  Accumulator Value: ', accumulator)
        break
    executedList[index] = True
    if (instrList[index][0] == 'nop'):
        index += 1
        continue
    if (instrList[index][0] == 'acc'):
        accumulator += int(instrList[index][1])
    if (instrList[index][0] == 'jmp'):
        index += int(instrList[index][1])
    else:
        index += 1
