import math


def sequence(i):
    n = 2 * i - 1
    return n * n


def layer(i):
    return math.floor((math.sqrt(i) + 1) / 2)


def length(i):
    return 8 * i


def sector(i):
    return math.floor(4 * (i - sequence(layer(i))) / length(layer(i)))


def position(i):
    l = layer(i)
    s = sector(i)
    offset = i - sequence(l) - s * length(l) // 4
    if s == 0.0:
        return -l, -l + offset + 1
    if s == 1.0:
        return -l + offset - 1, l
    if s == 2.0:
        return l, l - offset - 1
    return l - offset - 1, -l


def dist(n):
    if n == 1:
        return 0
    # everything is minus 1 so 265149 -> 265148
    n = n - 1
    pos = position(n)
    steps = abs(pos[0]) + abs(pos[1])
    return int(steps)


grid = """
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23  24  25
"""

assert dist(1) == 0
assert dist(12) == 3
assert dist(23) == 2
# TODO
# assert dist(1024) == 31

print dist(277678)
