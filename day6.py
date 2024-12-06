import copy
import sys


def walk(plan, pos):
    i, j = pos
    d = plan[i][j]
    while True:
        # (re)visit
        plan[i][j] = 'X'
        # then, stop
        if d == '^' and i == 0:
            break
        if d == '<' and j == 0:
            break
        if d == '>' and j == len(plan[0]) - 1:
            break
        if d == 'v' and i == len(plan) - 1:
            break
        # or update to next position!
        if d == '^':
            if plan[i - 1][j] == '#':
                d = '>'
            else:
                i -= 1
        if d == 'v':
            if plan[i + 1][j] == '#':
                d = '<'
            else:
                i += 1
        if d == '<':
            if plan[i][j - 1] == '#':
                d = '^'
            else:
                j -= 1
        if d == '>':
            if plan[i][j + 1] == '#':
                d = 'v'
            else:
                j += 1
    return plan


def doesloop(plan, pos):
    i, j = pos
    d = plan[i][j]
    plan[i][j] = '.'
    while True:
        # visit or detect loop
        if d in plan[i][j]:
            print(f"Reached {i},{j} with {plan[i][j]} while going {d}")
            return True
        else:
            plan[i][j] += d
        # then, stop
        if d == '^' and i == 0:
            break
        if d == '<' and j == 0:
            break
        if d == '>' and j == len(plan[0]) - 1:
            break
        if d == 'v' and i == len(plan) - 1:
            break
        # or update to next position!
        if d == '^':
            if plan[i - 1][j] == '#':
                d = '>'
            else:
                i -= 1
        if d == 'v':
            if plan[i + 1][j] == '#':
                d = '<'
            else:
                i += 1
        if d == '<':
            if plan[i][j - 1] == '#':
                d = '^'
            else:
                j -= 1
        if d == '>':
            if plan[i][j + 1] == '#':
                d = 'v'
            else:
                j += 1
    return False


def silver(fname):
    plan = []
    with open(fname, "r") as f:
        for line in f:
            line = line.strip()
            plan.append([elem for elem in line])

    # Let's find the current position
    found = False
    for i in range(len(plan)):
        for j in range(len(plan[0])):
            if plan[i][j] in ['^', 'v', '>', '<']:
                pos = (i, j)
                found = True
                break
        if found:
            break
    print(f"Current position {pos}")

    # Let's walk the walk
    plan = walk(plan, pos)
    plan = list(map(lambda x: "".join(x), plan))
    print("\n".join(plan))

    return sum(map(lambda x: 1 if x == 'X' else 0, "".join(plan)))


def gold(fname):
    plan = []
    with open(fname, "r") as f:
        for line in f:
            line = line.strip()
            plan.append([elem for elem in line])

    # Let's find the current position
    found = False
    for i in range(len(plan)):
        for j in range(len(plan[0])):
            if plan[i][j] in ['^', 'v', '>', '<']:
                pos = (i, j)
                found = True
                break
        if found:
            break
    print(f"Current position {pos}")

    # Let's walk the walk
    firstplan = copy.deepcopy(plan)
    plan = walk(plan, pos)
    opts = []
    for i in range(len(plan)):
        for j in range(len(plan[0])):
            if plan[i][j] == 'X' and (i, j) != pos:
                opts.append(tuple([i, j]))
    # restore the plan
    plan = firstplan

    # Check which options cause a loop
    looped = 0
    for n, o in enumerate(opts):
        newplan = copy.deepcopy(plan)
        i, j = o
        newplan[i][j] = '#'
        print(f"{n+1}/{len(opts)}: Trying obstacle at {o}")
        if doesloop(newplan, pos):
            looped += 1

    return looped


if __name__ == "__main__":
    fname = "day6.txt"
    if len(sys.argv) > 1 and sys.argv[1] == '-g':
        res = gold(fname)
    else:
        res = silver(fname)
    print(f"Result {res}")
