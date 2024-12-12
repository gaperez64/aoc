import itertools
import copy
import sys


def silver(fname):
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
        hors = {}
        vert = {}
        while len(tovisit) > 0:
            (i, j) = tovisit.pop()
            for (a, b) in [(i + 1, j), (i - 1, j),
                           (i, j + 1), (i, j - 1)]:
                if a < 0 or a >= len(plan):
                    per += 1
                    if a + 1 in hors:
                        hors[a + 1].add(j)
                    else:
                        hors[a + 1] = set([j])
                elif b < 0 or b >= len(plan[0]):
                    per += 1
                    if b + 1 in vert:
                        vert[b + 1].add(i)
                    else:
                        vert[b + 1] = set([i])
                elif plan[a][b] != plan[x][y]:
                    per += 1
                    if a != i:
                        if a + 1 in hors:
                            hors[a + 1].add(j)
                        else:
                            hors[a + 1] = set([j])
                    else:
                        if b + 1 in vert:
                            vert[b + 1].add(i)
                        else:
                            vert[b + 1] = set([i])
                elif (a, b) not in visited:
                    tovisit.append(tuple([a, b]))
                    visited[(a, b)] = True
                    cnt += 1
        print(f"Region of {plan[x][y]} has area {cnt} and perimenter {per}")
        return cnt, per

    total = 0
    for i in range(len(plan)):
        for j in range(len(plan[0])):
            if (i, j) not in visited:
                area, perimeter = visit(i, j)
                total += area * perimeter
    return total


def gold(fname):
    pass


if __name__ == "__main__":
    fname = "day12.txt"
    if len(sys.argv) > 1 and sys.argv[1] == '-g':
        res = gold(fname)
    else:
        res = silver(fname)
    print(f"Result {res}")
