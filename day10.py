import itertools
import copy
import sys


def silver(fname):
    plan = []
    with open(fname, "r") as f:
        for line in f:
            line = line.strip()
            plan.append([int(elem) for elem in line])
    print(plan)

    def neighborhood(x, y, backwards=True):
        mx = len(plan)
        my = len(plan[0])
        res = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        res = [(x, y) for (x, y) in res
               if (x >= 0 and x < mx and y >= 0 and y < my)]
        if backwards:
            d = -1
        else:
            d = 1
        res = [(i, j) for (i, j) in res
               if (plan[i][j] - plan[x][y] == d)]
        return res

    vals = {}
    start = []
    c = 0
    for i in range(len(plan)):
        for j in range(len(plan[0])):
            if plan[i][j] == 9:
                loc = (i, j)
                vals[loc] = (1 << c)
                start.extend(neighborhood(*loc))
                c += 1
            else:
                vals[(i, j)] = 0
    print(vals)

    tocheck = copy.deepcopy(start)
    while len(tocheck) > 0:
        loc = tocheck.pop()
        oldvals = vals[loc]
        for n in neighborhood(*loc, backwards=False):
            vals[loc] |= vals[n]
        if oldvals != vals[loc]:
            tocheck.extend(neighborhood(*loc))

    total = 0
    for i in range(len(plan)):
        for j in range(len(plan[0])):
            if plan[i][j] == 0:
                total += vals[(i, j)].bit_count()

    return total


def gold(fname):
    plan = []
    with open(fname, "r") as f:
        for line in f:
            line = line.strip()
            plan.append([int(elem) for elem in line])
    print(plan)

    def neighborhood(x, y, backwards=True):
        mx = len(plan)
        my = len(plan[0])
        res = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        res = [(x, y) for (x, y) in res
               if (x >= 0 and x < mx and y >= 0 and y < my)]
        if backwards:
            d = -1
        else:
            d = 1
        res = [(i, j) for (i, j) in res
               if (plan[i][j] - plan[x][y] == d)]
        return res

    vals = {}
    start = []
    for i in range(len(plan)):
        for j in range(len(plan[0])):
            if plan[i][j] == 9:
                loc = (i, j)
                vals[loc] = 1
                start.extend(neighborhood(*loc))
            else:
                vals[(i, j)] = 0
    print(vals)

    tocheck = copy.deepcopy(start)
    while len(tocheck) > 0:
        loc = tocheck.pop()
        oldvals = vals[loc]
        vals[loc] = 0
        for n in neighborhood(*loc, backwards=False):
            vals[loc] += vals[n]
        if oldvals != vals[loc]:
            tocheck.extend(neighborhood(*loc))

    total = 0
    for i in range(len(plan)):
        for j in range(len(plan[0])):
            if plan[i][j] == 0:
                total += vals[(i, j)]

    return total


if __name__ == "__main__":
    fname = "day10.txt"
    if len(sys.argv) > 1 and sys.argv[1] == '-g':
        res = gold(fname)
    else:
        res = silver(fname)
    print(f"Result {res}")
