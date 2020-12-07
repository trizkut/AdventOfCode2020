myList = []
for line in open('inputs/input1.txt'):
    myList.append(int(line))

myList.sort()
found = False
for i in range(0,199):
    for j in range(0,199):
        for k in range(0,199):
            if ((myList[i] + myList[j] + myList[k]) == 2020):
                print(myList[i])
                print(myList[j])
                print(myList[k])
                print(myList[i]*myList[j]*myList[k])
                found = True
                break
        if (found):
            break

    if (found):
        break