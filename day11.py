import itertools
import copy
import sys


def blink(n):
    if n == 0:
        return [1]
    elif len(str(n)) % 2 == 0:
        sn = str(n)
        return [int(sn[:len(sn) // 2]),
                int(sn[len(sn) // 2:])]
    else:
        return [n * 2024]


def silver(fname, days=25):
    nums = []
    with open(fname, "r") as f:
        for line in f:
            line = line.strip()
            nums = [int(n) for n in line.split()]
    print(nums)

    todo = [(n, days) for n in nums]
    cache = {}
    while len(todo) > 0:
        n, i = todo.pop()
        if i == 0:
            cache[(n, i)] = 1
            continue
        succ = [(m, i - 1) for m in blink(n)]
        done = True
        total = 0
        for s in succ:
            if s not in cache:
                done = False
                todo.append(tuple([n, i]))
                todo.append(s)
                break
            else:
                total += cache[s]
        if done:
            cache[(n, i)] = total

    return sum([cache[(n, days)] for n in nums])


def gold(fname):
    return silver(fname, days=75)


if __name__ == "__main__":
    fname = "day11.txt"
    if len(sys.argv) > 1 and sys.argv[1] == '-g':
        res = gold(fname)
    else:
        res = silver(fname)
    print(f"Result {res}")
