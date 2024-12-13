from collections import defaultdict
import copy
import itertools
import sys


def nointsol(a, b, target):
    c = (a[0] * a[1], 0)
    d = (b[0] * a[1], b[1] * a[0] - b[0] * a[1])
    t = (target[0] * a[1],
         target[1] * a[0] - target[0] * a[1])
    if d[1] == 0:
        return False
    if t[1] % d[1] != 0:
        return True
    xd = t[1] // d[1]
    if (t[0] - xd * d[0]) % c[0] != 0:
        return True
    return False


def silver(fname, shift=0):
    machines = []
    with open(fname, "r") as f:
        a = None
        b = None
        p = None
        for line in f:
            line = line.strip()
            if line == "":
                machines.append(tuple([a, b, p]))
                continue
            dirs = line.split(":")[1].split(",")
            dirs = tuple(map(lambda x: int(x.strip()[2:]), dirs))
            if "Button A" in line:
                a = dirs
            elif "Button B" in line:
                b = dirs
            elif "Prize" in line:
                p = dirs
            else:
                assert False
        # and one last time
        machines.append(tuple([a, b, p]))
    # print(machines)

    total = 0
    i = 1
    for (a, b, target) in machines:
        target = (target[0] + shift, target[1] + shift)
        prices = []
        # Quick check for integer solutions based on a manual Smith form
        if nointsol(a, b, target):
            continue

        # There's at least one integer solution, let's search!
        x = 0
        y = 0
        na = 0
        nb = 0
        # Max out on A
        na = min(target[0] // a[0], target[1] // a[1])
        x += a[0] * na
        y += a[1] * na
        # Max the rest on B
        nb = min((target[0] - x) // b[0], (target[1] - y) // b[1])
        x += b[0] * nb
        y += b[1] * nb
        while na > 0:
            if x == target[0] and y == target[1]:
                prices.append(3 * na + 1 * nb)
                if len(prices) >= 2 and prices[-1] >= prices[-2]:
                    break
            # Drop one A
            x -= a[0]
            y -= a[1]
            na -= 1
            # Quick check for integer solutions based on a manual Smith form
            if nointsol(a, b, (target[0] - a[0] * na, target[1] - a[1] * na)):
                break
            # Max it out again on B
            mb = min((target[0] - x) // b[0], (target[1] - y) // b[1])
            nb += mb
            x += b[0] * mb
            y += b[1] * mb
        # print(prices)
        print(f"Machine {i} / {len(machines)} done!")
        i += 1
        if len(prices) > 0:
            total += min(prices)

    return total


def gold(fname):
    shift = 10000000000000
    machines = []
    with open(fname, "r") as f:
        a = None
        b = None
        p = None
        for line in f:
            line = line.strip()
            if line == "":
                machines.append(tuple([a, b, p]))
                continue
            dirs = line.split(":")[1].split(",")
            dirs = tuple(map(lambda x: int(x.strip()[2:]), dirs))
            if "Button A" in line:
                a = dirs
            elif "Button B" in line:
                b = dirs
            elif "Prize" in line:
                p = dirs
            else:
                assert False
        # and one last time
        machines.append(tuple([a, b, p]))
    # print(machines)

    total = 0
    for (a, b, target) in machines:
        target = (target[0] + shift, target[1] + shift)
        numx = target[0] * b[1] - b[0] * target[1]
        denx = a[0] * b[1] - b[0] * a[1]
        if numx % denx != 0:
            continue
        x = numx // denx
        numy = a[0] * target[1] - target[0] * a[1]
        deny = a[0] * b[1] - b[0] * a[1]
        if numy % deny != 0:
            continue
        y = numy // deny
        total += 3 * x + 1 * y

    return total


if __name__ == "__main__":
    fname = "day13.txt"
    if len(sys.argv) > 1 and sys.argv[1] == '-g':
        res = gold(fname)
    else:
        res = silver(fname)
    print(f"Result {res}")
