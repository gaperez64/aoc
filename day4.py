import re
import sys


xmasre = re.compile("(?=(XMAS|SAMX))")


def occurrences(rows):
    total = 0
    for r in rows:
        start = 0
        while True:
            start = r.find("XMAS", start) + 1
            if start > 0:
                total += 1
            else:
                break
        start = 0
        while True:
            start = r.find("SAMX", start) + 1
            if start > 0:
                total += 1
            else:
                break
    return total


def transpose(horz):
    assert (len(horz) == len(horz[0]))
    for i in range(len(horz)):
        assert (len(horz[i]) == len(horz[0]))
    vert = []
    for j in range(len(horz[0])):
        col = ""
        for i in range(len(horz)):
            col += horz[i][j]
        vert.append(col)
    return vert


def getdiag(horz):
    assert (len(horz) == len(horz[0]))
    for i in range(len(horz)):
        assert (len(horz[i]) == len(horz[0]))
    diag = []
    for s in reversed(range(len(horz[0]))):
        i = 0
        j = s
        temp = ""
        while i < len(horz) and j < len(horz[0]):
            temp += horz[i][j]
            i += 1
            j += 1
        diag.append(temp)
    for s in range(1, len(horz)):
        i = s
        j = 0
        temp = ""
        while i < len(horz) and j < len(horz[0]):
            temp += horz[i][j]
            i += 1
            j += 1
        diag.append(temp)
    assert len(diag) == len(horz) * 2 - 1
    return diag


def antidiag(horz):
    assert (len(horz) == len(horz[0]))
    for i in range(len(horz)):
        assert (len(horz[i]) == len(horz[0]))
    diag = []
    for s in range(len(horz)):
        i = s
        j = 0
        temp = ""
        while i >= 0 and j < len(horz[0]):
            temp += horz[i][j]
            i -= 1
            j += 1
        diag.append(temp)
    for s in range(1, len(horz[0])):
        i = len(horz) - 1
        j = s
        temp = ""
        while i >= 0 and j < len(horz[0]):
            temp += horz[i][j]
            i -= 1
            j += 1
        diag.append(temp)
    assert len(diag) == len(horz) * 2 - 1
    return diag


def silver(fname):
    horz = []
    with open(fname, "r") as f:
        for line in f:
            line = line.strip()
            horz.append(line)

    # Solution
    diag = getdiag(horz)
    vert = transpose(horz)
    diag2 = antidiag(vert)

    assert horz == transpose(vert)

    print("ORIGINAL")
    print("\n".join(horz))
    print(occurrences(horz))
    print("ANTI DIAGONAL")
    print("\n".join(diag2))
    print(occurrences(diag2))
    print("DIAGONAL")
    print("\n".join(diag))
    print(occurrences(diag))
    print("VERTICAL")
    print("\n".join(vert))
    print(occurrences(vert))

    return occurrences(horz + diag + vert + diag2)


def gold(fname):
    horz = []
    with open(fname, "r") as f:
        for line in f:
            line = line.strip()
            horz.append(line)

    total = 0
    for i in range(1, len(horz) - 1):
        for j in range(1, len(horz[0]) - 1):
            if horz[i][j] == "A":
                ox = 0
                for a, b, k, l in [(i-1, j-1, i+1, j+1),
                                   (i-1, j+1, i+1, j-1)]:
                    chars = [horz[a][b], horz[k][l]]
                    if 'M' in chars and 'S' in chars:
                        ox += 1
                if ox == 2:
                    total += 1
                    print("\n".join(map(lambda r: r[j-1:j+2], horz[i-1:i+2])))
                    print("")
    return total


if __name__ == "__main__":
    fname = "day4.txt"
    if len(sys.argv) > 1 and sys.argv[1] == '-g':
        res = gold(fname)
    else:
        res = silver(fname)
    print(f"Result {res}")
