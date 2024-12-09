import itertools
import copy
import sys


def silver(fname):
    plan = []
    with open(fname, "r") as f:
        for line in f:
            line = line.strip()
            plan.append([elem for elem in line])
    assert len(plan) == 1
    plan = plan[0]

    # Expand
    mem = []
    cidx = 0
    content = True
    for i in plan:
        if content:
            mem.extend([str(cidx)] * int(i))
            cidx += 1
        else:
            mem.extend(['.'] * int(i))
        content = not content

    # Defrag
    i = 0
    j = len(mem) - 1
    while True:
        while i < j and mem[i] != '.':
            i += 1
        while i < j and mem[j] == '.':
            j -= 1
        if i < j:
            mem[i] = mem[j]
            mem[j] = '.'
        else:
            break
    print("".join(mem))

    # Checksum
    total = 0
    for i, el in enumerate(mem):
        if el == '.':
            break
        else:
            total += i * int(el)
    return total


def gold(fname):
    plan = []
    with open(fname, "r") as f:
        for line in f:
            line = line.strip()
            plan.append([elem for elem in line])
    assert len(plan) == 1
    plan = plan[0]

    # Expand
    mem = []
    cidx = 0
    content = True
    for i in plan:
        if content:
            mem.append([str(cidx)] * int(i))
            cidx += 1
        else:
            d = int(i)
            if d > 0:
                mem.append(['.'] * d)
        content = not content

    # Defrag
    done = set()
    j = len(mem) - 1
    while True:
        i = 0
        while i < j and (mem[j][0] == '.' or
                         mem[j][0] in done):
            j -= 1
        if j == 0:
            break
        while i < j and (mem[i][0] != '.' or
                         len(mem[i]) < len(mem[j])):
            i += 1
        if i < j:
            done.add(mem[j][0])
            print(f"Trying to move a block of {mem[j][0]} x {len(mem[j])}")
            diff = len(mem[i]) - len(mem[j])
            mem[i] = mem[j]
            mem[j] = ['.'] * len(mem[j])
            print(f"Moved it to {i}: {mem[i]}")
            if diff > 0:
                mem.insert(i + 1, ['.'] * diff)
                print(f"Remaining space to {i+1}: {mem[i+1]}")
        else:
            j -= 1

    # Checksum
    mem = list(itertools.chain.from_iterable(mem))
    total = 0
    for i, el in enumerate(mem):
        if el == '.':
            continue
        else:
            total += i * int(el)
    return total


if __name__ == "__main__":
    fname = "day9.txt"
    if len(sys.argv) > 1 and sys.argv[1] == '-g':
        res = gold(fname)
    else:
        res = silver(fname)
    print(f"Result {res}")
