import sys


def issafe(s):
    incs = 0
    decs = 0
    for j in range(1, len(s)):
        sgn = s[j] - s[j-1]
        abssgn = abs(sgn)
        if abssgn == 0 or abssgn > 3:
            continue
        else:
            print(f"|{s[j]} - {s[j-1]}| = {abssgn}")
        sgn = sgn // abs(sgn)
        if sgn == 1:
            incs += 1
        elif sgn == -1:
            decs += 1
        else:
            assert False
    # Time to check and count
    return incs >= (len(s) - 1) or decs >= (len(s) - 1)


def silver(fname):
    seqs = []
    with open(fname, "r") as f:
        for line in f:
            line = line.strip()
            seqs.append(map(lambda x: int(x.strip()),
                        line.split()))

    # Now, for the solution, we need to count safe seqs and safety depends on
    # the sign of the first difference
    safe = 0
    for s in seqs:
        s = list(s)
        sgn = s[1] - s[0]
        error = (0, 0)
        if sgn == 0 or abs(sgn) > 3:
            error = (0, 1)
        else:
            sgn = sgn // abs(sgn)
            # This should give me the sign
            assert sgn in [1, -1]
            # Now we just need to ensure bounds and signs
            unsafe = False
            for i in range(2, len(s)):
                diff = s[i] - s[i - 1]
                if diff == 0:
                    unsafe = True
                    error = (i - 1, i)
                    break
                absdiff = abs(diff)
                sgndiff = diff // absdiff
                if sgndiff != sgn:
                    unsafe = True
                    error = (i - 1, i)
                    break
                if absdiff > 3:
                    unsafe = True
                    error = (i - 1, i)
                    break
        # Time to check and count
        if unsafe:
            print(f"Unsafe {s}")
            s1 = s.copy()
            s1.pop(error[0])
            s2 = s.copy()
            s2.pop(error[1])
            s0 = s.copy()
            s0.pop(0)
            print(f"s1 = {s1}, s2 = {s2}")
            if issafe(s1) or issafe(s2) or issafe(s0):
                print("Now safe!")
                safe += 1
        else:
            safe += 1
    return safe


def gold(fname):
    pass


if __name__ == "__main__":
    fname = "day2.txt"
    if len(sys.argv) > 1 and sys.argv[1] == '-g':
        res = gold(fname)
    else:
        res = silver(fname)
    print(f"Result {res}")
