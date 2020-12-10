from collections import Counter


adapters = []




starting_joltage = 0  #charging port
for line in open('inputs/input10.txt', 'r'):
    adapters.append(int(line))

adapters.append(0) #starting node
device_joltage = max(adapters) + 3
adapters.sort()
#print(device_joltage)
#print(adapters)

i = 1
three_jolt_counter = 0
two_jolt_counter = 0
one_jolt_counter = 0
cur_joltage = starting_joltage
while (i < len(adapters)):
    #print(adapters[i], cur_joltage)
    if (adapters[i] - cur_joltage == 3):
        #print(adapters[i], cur_joltage)
        three_jolt_counter += 1
    if (adapters[i] - cur_joltage == 2):
        two_jolt_counter += 1
    if (adapters[i] - cur_joltage == 1):
        one_jolt_counter += 1
    cur_joltage = adapters[i]
    i += 1
three_jolt_counter += 1 # one 3-jolt jump to get to highest rating

print("One jolt differences: ", one_jolt_counter)
print("Three jolt differences: ", three_jolt_counter)
print("Device rated joltage:", device_joltage)
print("Product: ", one_jolt_counter * three_jolt_counter)



#find arrangements

adapters.remove(0)
adapters.append(device_joltage)


dp = Counter()
dp[0] = 1

for adapter in adapters:
    dp[adapter] = dp[adapter-1] + dp[adapter-2] + dp[adapter-3]

print(dp[adapters[-1]])

