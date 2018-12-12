import sys
from collections import defaultdict
from time import sleep

players = int(sys.argv[1])
last_marble = int(sys.argv[2])

marbles = [0]
scores = defaultdict(int)
curr_index = 1
for i in range(1, last_marble+1):
    if i % 23 == 0:
        to_remove = (curr_index - 7) % len(marbles)
        scores[i%players] += i + marbles[to_remove]
        marbles = marbles[:to_remove] + marbles[to_remove+1:]
        curr_index -= 7
    elif curr_index == len(marbles):
        marbles.append(i)
    else:
        curr_index += 2
        if curr_index > len(marbles):
            curr_index = 1
        marbles = marbles[:curr_index] + [i] + marbles[curr_index:]


high = 0
for k,v in scores.items():
    if v > high:
        high = v

print(high)
