import copy
import sys


def findAtns2(plan, i, j, atns):
    atnSym = plan[i][j]
    print(f"Adding antinodes for antenna {atnSym} at {i, j}")
    for k in range(i, len(plan)):
        for l in range(len(plan[0])):
            if k == i and l <= j:
                continue
            if plan[k][l] == atnSym:
                diff = (k - i, l - j)
                p = (i, j)
                while p[0] >= 0 and p[0] < len(plan) and\
                        p[1] >= 0 and p[1] < len(plan[0]):
                    atns[p[0]][p[1]] = '#'
                    p = (p[0] + diff[0], p[1] + diff[1])
                p = (i - diff[0], j - diff[1])
                while p[0] >= 0 and p[0] < len(plan) and\
                        p[1] >= 0 and p[1] < len(plan[0]):
                    atns[p[0]][p[1]] = '#'
                    p = (p[0] - diff[0], p[1] - diff[1])


def findAtns(plan, i, j, atns):
    atnSym = plan[i][j]
    print(f"Adding antinodes for antenna {atnSym} at {i, j}")
    for k in range(i, len(plan)):
        for l in range(len(plan[0])):
            if k == i and l <= j:
                continue
            if plan[k][l] == atnSym:
                diff = (k - i, l - j)
                pos1 = (diff[0] + k, diff[1] + l)
                pos2 = (i - diff[0], j - diff[1])
                for p in [pos1, pos2]:
                    if p[0] >= 0 and p[0] < len(plan) and\
                            p[1] >= 0 and p[1] < len(plan[0]):
                        atns[p[0]][p[1]] = '#'


def silver(fname, resonance=False):
    plan = []
    with open(fname, "r") as f:
        for line in f:
            line = line.strip()
            plan.append([elem for elem in line])

    erow = ['.' for _ in range(len(plan[0]))]
    atns = [copy.deepcopy(erow) for _ in range(len(plan))]

    for i in range(len(plan)):
        for j in range(len(plan[0])):
            if plan[i][j] != '.':
                if not resonance:
                    findAtns(plan, i, j, atns)
                else:
                    findAtns2(plan, i, j, atns)
    print("\n".join(map(lambda x: "".join(x), atns)))

    atnCnt = map(sum,
                 map(lambda x: [1 if c == '#' else 0 for c in x], atns))
    atnCnt = sum(atnCnt)
    return atnCnt


def gold(fname):
    return silver(fname, resonance=True)


if __name__ == "__main__":
    fname = "day8.txt"
    if len(sys.argv) > 1 and sys.argv[1] == '-g':
        res = gold(fname)
    else:
        res = silver(fname)
    print(f"Result {res}")
