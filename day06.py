from spitslurp import slurp
import json

memory = [0, 2, 7, 0]
# [0, 2, 7, 0]
# [2, 4, 1, 2]
# [3, 1, 2, 3]
# [0, 2, 3, 4]
# [1, 3, 4, 1]
# [2, 4, 1, 2] <- already seen in 1st iteration so stop


def next_idx(length, idx):
    idx = idx + 1
    idx = 0 if idx >= length else idx
    return idx


def balance(memory):
    length = len(memory)
    largest = max(memory)
    idx = memory.index(largest)
    # print largest, idx
    memory[idx] = 0
    while largest > 0:
        idx = next_idx(length, idx)
        # print idx
        memory[idx] = memory[idx] + 1
        largest = largest - 1
    return memory

# print memory
# print balance(memory)

memory = map(int, slurp('day06.txt').split())
states = set(memory)
steps = 0
while True:
    memory = balance(memory)
    steps = steps + 1
    if json.dumps(memory) in states:
        break
    else:
        states.add(json.dumps(memory))

print 'Part 1:', steps

# Part 2 - steps between identical states

memory = map(int, slurp('day06.txt').split())
states = [json.dumps(memory)]
steps = 0
while True:
    memory = balance(memory)
    try:
        first_time_seen = states.index(json.dumps(memory))
    except:
        first_time_seen = -1
    if first_time_seen > -1:
        steps = len(states) - first_time_seen
        break
    else:
        states.append(json.dumps(memory))

print 'Part 2:', steps
