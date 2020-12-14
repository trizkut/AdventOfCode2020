import math
lines = []
for line in open('inputs/input13.txt', 'r'):
    lines.append(line.strip())

timestamp = int(lines[0])
ids = lines[1].split(",")

print(timestamp, ids)
before, after = {}, {}
for id in ids:
    if (id != 'x'):
        bus = int(id)
        before[id] = math.floor(timestamp/bus) * bus
        after[id] = math.ceil(timestamp/bus) * bus


min = min(after.values())
wait_time = min-timestamp
for key in after:
    if after[key] == min:
        bus_id = int(key)
        break

print(bus_id * wait_time)

buses = [int(l) if l != "x" else None for l in lines[1].split(",")]
i = 0
while not all([(i + k) % b == 0 for k, b in enumerate(buses) if b]):
    l = [b for k, b in enumerate(buses) if b and (i + k) % b == 0] # find buses that already depart at correct offset of timestamp
    prod = 1
    for b in l: # increment by multiples of buses already in sync
        prod *= b
    i += prod

print(i)