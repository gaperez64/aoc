from collections import defaultdict
import copy
from functools import reduce
import itertools
import operator
import sys


def prod(iterable):
    return reduce(operator.mul, iterable, 1)


def silver(fname, shift=0):
    machines = []
    with open(fname, "r") as f:
        for line in f:
            line = line.strip()
            p, v = line.split()
            p = tuple(map(int, p[2:].split(",")))
            v = tuple(map(int, v[2:].split(",")))
            machines.append(tuple([p, v]))
    # print(machines)

    simtime = 100
    dimx = 101
    dimy = 103
    quads = [[], [], [], []]
    for (p, v) in machines:
        (x, y) = p
        (dx, dy) = v
        x = (x + simtime * dx) % dimx
        y = (y + simtime * dy) % dimy
        if x < (dimx - 1) // 2 and y < (dimy - 1) // 2:
            quads[0].append(tuple([x, y]))
        elif x > (dimx - 1) // 2 and y < (dimy - 1) // 2:
            quads[1].append(tuple([x, y]))
        elif x > (dimx - 1) // 2 and y > (dimy - 1) // 2:
            quads[2].append(tuple([x, y]))
        elif x < (dimx - 1) // 2 and y > (dimy - 1) // 2:
            quads[3].append(tuple([x, y]))
        else:
            print(f"Ignoring ({x}, {y})")
    print(quads)

    return prod(map(len, quads))


def gold(fname):
    pass


if __name__ == "__main__":
    fname = "day14.txt"
    if len(sys.argv) > 1 and sys.argv[1] == '-g':
        res = gold(fname)
    else:
        res = silver(fname)
    print(f"Result {res}")
