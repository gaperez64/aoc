import re
import sys


muls = re.compile(r"mul\((\d+),(\d+)\)")
dore = re.compile(r"do\(\)")
dontre = re.compile(r"don't\(\)")


def parse(seqs):
    # Now for the solution
    results = []
    for s in seqs:
        summands = map(lambda p: int(p[0]) * int(p[1]), muls.findall(s))
        results.append(sum(summands))
    print(f"Summands per line {results}")
    return sum(results)


def silver(fname):
    seqs = []
    with open(fname, "r") as f:
        for line in f:
            line = line.strip()
            seqs.append(line)
    return parse(seqs)


def gold(fname):
    seqs = []
    with open(fname, "r") as f:
        for line in f:
            line = line.strip()
            seqs.append(line)

    # Before I parse, I need to disable stuff
    clean = []
    for s in seqs:
        start = dontre.search(s)
        while start is not None:
            start = start.start()
            end = dore.search(s, start - 1)
            if end is None:
                print(f"Removed {s[start:]}")
                s = s[:start]
            else:
                end = end.start()
                print(f"Removed {s[start:end]}")
                s = s[:start] + s[end:]
            start = dontre.search(s)
        print(f"Clean line: {s}")
        clean.append("" + s)
    print(" == CLEAN == ")
    print(clean)

    # Now we're ready
    return parse(clean)


if __name__ == "__main__":
    fname = "day3.txt"
    if len(sys.argv) > 1 and sys.argv[1] == '-g':
        res = gold(fname)
    else:
        res = silver(fname)
    print(f"Result {res}")
