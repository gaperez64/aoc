import sys


def silver(fname):
    prohibd = {}
    pages = []
    with open(fname, "r") as f:
        rules = True
        for line in f:
            line = line.strip()
            if line == "":  # end of rules
                rules = False
                continue
            if rules:
                l, r = tuple(map(int, line.split("|")))
                if r not in prohibd:
                    prohibd[r] = []
                prohibd[r].append(l)
            else:
                pages.append(list(map(int, line.split(","))))
    # print(prohibd)
    # print(pages)

    # Solution
    correct = []
    for p in pages:
        avoid = set()
        prob = False
        for x in p:
            if x in avoid:
                prob = True
                break
            elif x in prohibd:
                avoid.update(prohibd[x])
        if not prob:
            correct.append(p)
    # print(correct)
    assert all(map(lambda c: len(c) % 2 == 1, correct))
    mids = map(lambda c: c[(len(c) - 1) // 2], correct)
    return sum(mids)


def gold(fname):
    prohibd = {}
    pages = []
    with open(fname, "r") as f:
        rules = True
        for line in f:
            line = line.strip()
            if line == "":  # end of rules
                rules = False
                continue
            if rules:
                l, r = tuple(map(int, line.split("|")))
                if r not in prohibd:
                    prohibd[r] = []
                prohibd[r].append(l)
            else:
                pages.append(list(map(int, line.split(","))))
    # print(prohibd)
    # print(pages)

    # Solution
    incorrect = []
    for p in pages:
        fixes = 0
        prob = True
        while prob:
            avoid = {}
            prob = False
            for pos, x in enumerate(p):
                if x in avoid:
                    prob = True
                    # Here is a local fix
                    (orig, opos) = avoid[x]
                    p[opos] = x
                    p[pos] = orig
                    fixes += 1
                    break
                elif x in prohibd:
                    for y in prohibd[x]:
                        avoid[y] = (x, pos)
        if fixes > 0:
            incorrect.append(p)
    print(incorrect)
    assert all(map(lambda c: len(c) % 2 == 1, incorrect))
    mids = map(lambda c: c[(len(c) - 1) // 2], incorrect)
    return sum(mids)


if __name__ == "__main__":
    fname = "day5.txt"
    if len(sys.argv) > 1 and sys.argv[1] == '-g':
        res = gold(fname)
    else:
        res = silver(fname)
    print(f"Result {res}")
