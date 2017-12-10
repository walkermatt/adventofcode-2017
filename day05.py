from spitslurp import slurp

# (0) 3  0  1  -3  - before we have taken any steps.
# (1) 3  0  1  -3  - jump with offset 0 (that is, don't jump at all). Fortunately, the instruction is then incremented to 1.
#  2 (3) 0  1  -3  - step forward because of the instruction we just modified. The first instruction is incremented again, now to 2.
#  2  4  0  1 (-3) - jump all the way to the end; leave a 4 behind.
#  2 (4) 0  1  -2  - go back to where we just were; increment -3 to -2.
#  2  5  0  1  -2  - jump 4 steps forward, escaping the maze.


def escape(offsets):
    steps = 0
    idx = 0
    try:
        while True:
            val = offsets[idx]
            # print 'val', val
            offsets[idx] = val + 1
            # print 'offsets', offsets
            idx = idx + val
            steps = steps + 1
    except IndexError:
        pass
    return steps

assert escape([0, 3, 0, 1, -3]) == 5

print 'Part 1:', escape(map(int, slurp('day05.txt').strip().split('\n')))


def escape2(offsets):
    steps = 0
    idx = 0
    try:
        while True:
            val = offsets[idx]
            # print 'val', val
            if val >= 3:
                offsets[idx] = val - 1
            else:
                offsets[idx] = val + 1
            # print 'offsets', offsets
            idx = idx + val
            steps = steps + 1
    except IndexError:
        pass
    return steps

assert escape2([0, 3, 0, 1, -3]) == 10

print 'Part 2:', escape2(map(int, slurp('day05.txt').strip().split('\n')))
