import sys
from itertools import repeat

def gen_combinations(ref, i=0, start=""):
    if i == len(ref):
        yield start
        return
    if ref[i] != '#':
        yield from gen_combinations(ref, i+1, start+'.')
    if ref[i] != '.':
        yield from gen_combinations(ref, i+1, start+'#')

def arrangements(line):
    print(f"checking {line}")
    [records, checks] = line.strip().split()
    checks: list[int] = [int(v) for v in checks.split(',')]
    checks = checks * 5
    records = '?'.join([records] * 5)
    P = len(records)
    G = len(checks)
    dp_op = [[0] * G for _ in range(P)]
    dp_br = [[0] * G for _ in range(P)]

    if records.count('#') > 0:
        min_hash_index = records.index('#')
    else:
        min_hash_index = P
    for p in range(P):
        for g in range(G):
            if p > 0:
                if records[p] != '#':
                    dp_br[p][g] += dp_br[p-1][g]
                    dp_br[p][g] += dp_op[p-1][g]
            #print(f"checks {checks[g]}")
            if records[p] != '.':
                if ((p >= checks[g] and records[p - checks[g]] != '#')
                    or (g == 0 and p == checks[0] - 1)):
                    if all(records[z] != '.' for z in range(p-checks[g]+1, p+1)):
                        if g > 0:
                            dp_op[p][g] = dp_br[p - checks[g]][g-1]
                        elif g == 0 and min_hash_index > p - checks[g]:
                            dp_op[p][g] = 1

            #print(f"P {p} G {g} op {dp_op[p][g]} br {dp_br[p][g]}")
    n = 0
    if records[-1] != '.':
        n += dp_op[P-1][G-1]
    if records[-1] != '#':
        n += dp_br[P-1][G-1]
    print(f"arrangements: {n}")
    return n

def main():
    S = 0
    for i, line in enumerate(sys.stdin):
        print(f"Line {i+1}")
        S += arrangements(line)
    print(f"SUM {S}")

if __name__ == "__main__":
    main()