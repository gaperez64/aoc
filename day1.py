from collections import Counter
import sys


def silver(fname):
    pairs = []
    with open(fname, "r") as f:
        for line in f:
            line = line.strip()
            pairs.append(map(lambda x: int(x.strip()),
                             line.split()))

    # Now for the solution
    f, s = zip(*pairs)
    f = sorted(f)
    s = sorted(s)
    pairs = list(zip(f, s))
    diffs = map(lambda p: abs(p[0] - p[1]), pairs)
    return sum(diffs)


def gold(fname):
    pairs = []
    with open(fname, "r") as f:
        for line in f:
            line = line.strip()
            pairs.append(map(lambda x: int(x.strip()),
                             line.split()))

    # Now for the solution
    f, s = zip(*pairs)
    f = Counter(f)
    s = Counter(s)
    sim = 0
    for k in f:
        sim += k * f[k] * s[k]
    return sim


if __name__ == "__main__":
    fname = "day1.txt"
    if len(sys.argv) > 1 and sys.argv[1] == '-g':
        res = gold(fname)
    else:
        res = silver(fname)
    print(f"Result {res}")
