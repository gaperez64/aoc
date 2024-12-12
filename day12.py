from collections import defaultdict
import copy
import itertools
import sys


def silver(fname, usesides=False):
    plan = []
    with open(fname, "r") as f:
        for line in f:
            line = line.strip()
            plan.append([elem for elem in line])

    visited = {}

    def visit(x, y):
        tovisit = [(x, y)]
        visited[(x, y)] = True
        per = 0
        cnt = 1
        hors = defaultdict(list)
        vert = defaultdict(list)
        while len(tovisit) > 0:
            (i, j) = tovisit.pop()
            for (a, b) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if a < 0 or a >= len(plan):
                    per += 1
                    hors[a].append(j)
                elif b < 0 or b >= len(plan[0]):
                    per += 1
                    vert[b].append(i)
                elif plan[a][b] != plan[x][y]:
                    per += 1
                    if a != i:
                        hors[i + (a - i) / 4].append(j)
                    else:
                        vert[j + (b - j) / 4].append(i)
                elif (a, b) not in visited:
                    tovisit.append(tuple([a, b]))
                    visited[(a, b)] = True
                    cnt += 1

        # Now, per key in hors and vert, we need to sort and find gaps
        sides = 0
        print(hors)
        for key in hors:
            assert len(hors[key]) > 0
            last = -2
            for el in sorted(hors[key]):
                if el - last > 1:
                    sides += 1
                last = el
        print(vert)
        for key in vert:
            assert len(vert[key]) > 0
            last = -2
            for el in sorted(vert[key]):
                if el - last > 1:
                    sides += 1
                last = el

        print(f"Region of {plan[x][y]}: area {cnt}, per {per}, sides {sides}")
        return cnt, per, sides

    total = 0
    for i in range(len(plan)):
        for j in range(len(plan[0])):
            if (i, j) not in visited:
                area, perimeter, sides = visit(i, j)
                if usesides:
                    total += area * sides
                else:
                    total += area * perimeter
    return total


def gold(fname):
    return silver(fname, usesides=True)


if __name__ == "__main__":
    fname = "day12.txt"
    if len(sys.argv) > 1 and sys.argv[1] == '-g':
        res = gold(fname)
    else:
        res = silver(fname)
    print(f"Result {res}")
