import sys


def silver(fname, cond_too=False):
    eqs = []
    with open(fname, "r") as f:
        for line in f:
            line = line.strip()
            tval, ops = line.split(":")
            tval = int(tval)
            ops = list(map(int, ops.split()))
            eqs.append(tuple([tval, ops]))

    # Solution
    valid = []
    for (tval, ops) in eqs:
        results = [ops[0]]
        for i in range(1, len(ops)):
            muld = map(lambda r: r * ops[i], results)
            sumd = map(lambda r: r + ops[i], results)
            if cond_too:
                cond = map(lambda r: int(str(r) + str(ops[i])), results)
            else:
                cond = []
            results = set([r for r in list(muld) + list(sumd) + list(cond)
                           if r <= tval])
        if tval in results:
            valid.append(tval)
    print(valid)

    return sum(valid)


def gold(fname):
    return silver(fname, cond_too=True)


if __name__ == "__main__":
    fname = "day7.txt"
    if len(sys.argv) > 1 and sys.argv[1] == '-g':
        res = gold(fname)
    else:
        res = silver(fname)
    print(f"Result {res}")
