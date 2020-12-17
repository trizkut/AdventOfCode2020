max_turns = 30000000
startingnumbers = []

for line in open('inputs/input15.txt', 'r'):
    startingnumbers = [int(s) for s in line.strip().split(",")]

last_spoken = {}

i = 1

for n in startingnumbers[:-1]:
    last_spoken[n] = i
    i += 1

spoken_word = startingnumbers[-1]
turn = i+1
while (turn <= max_turns):

    if (spoken_word in last_spoken):
        diff = turn - 1 - last_spoken[spoken_word]
        last_spoken[spoken_word] = turn - 1
        spoken_word = diff
    else:
        last_spoken[spoken_word] = turn - 1
        spoken_word = 0

    turn += 1

print(spoken_word)
