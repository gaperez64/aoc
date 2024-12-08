import sys


def transpose(M):
    rows = []
    for j in range(len(M[0])):
        r = []
        for i in range(len(M)):
            r.append(M[i][j])
        rows.append(r)
    return rows


def encode(M):
    cur = []
    for row in M:
        val = 0
        for c in row:
            val = val * 2 + (1 if c == '#' else 0)
        cur.append(val)
    return cur


def bits_diff(b1, b2):
    r = b1 ^ b2
    return r.bit_count()


def first_ref(encs, diff=0):
    for i in range(1, len(encs)):
        start = max(0, 2 * i - len(encs))
        end = min(len(encs), 2 * i)
        l1 = encs[start:i]
        l2 = reversed(encs[i:end])
        totdiff = sum(map(lambda bs: bits_diff(*bs), zip(l1, l2)))
        if totdiff == diff:
            return i
    return None


def silver(fname):
    pats = []
    cur = []
    with open(fname, "r") as f:
        for line in f:
            line = line.strip()
            if line != "":
                cur.append([c for c in line])
            else:
                pats.append(cur)
                cur = []
    if len(cur) > 0:
        pats.append(cur)

    for p in pats:
        print("\n".join(map(lambda x: "".join(x), p)))
        print("==")

    # Solution
    encs = []
    tencs = []
    for p in pats:
        encs.append(encode(p))
        tencs.append(encode(transpose(p)))

    for i in range(len(encs)):
        print(encs[i])
        print("TT")
        print(tencs[i])
        print("==")

    total = 0
    for i in range(len(encs)):
        res = first_ref(tencs[i])
        if res is not None:
            total += res
        res = first_ref(encs[i])
        if res is not None:
            total += 100 * res

    return total


def gold(fname):
    pats = []
    cur = []
    with open(fname, "r") as f:
        for line in f:
            line = line.strip()
            if line != "":
                cur.append([c for c in line])
            else:
                pats.append(cur)
                cur = []
    if len(cur) > 0:
        pats.append(cur)

    for p in pats:
        print("\n".join(map(lambda x: "".join(x), p)))
        print("==")

    # Solution
    encs = []
    tencs = []
    for p in pats:
        encs.append(encode(p))
        tencs.append(encode(transpose(p)))

    for i in range(len(encs)):
        print(encs[i])
        print("TT")
        print(tencs[i])
        print("==")

    total = 0
    for i in range(len(encs)):
        res = first_ref(tencs[i], diff=1)
        if res is not None:
            total += res
        res = first_ref(encs[i], diff=1)
        if res is not None:
            total += 100 * res

    return total


if __name__ == "__main__":
    fname = "night13.txt"
    if len(sys.argv) > 1 and sys.argv[1] == '-g':
        res = gold(fname)
    else:
        res = silver(fname)
    print(f"Result {res}")
