import sys

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
    checks = [int(v) for v in checks.split(',')]
    n = 0
    for g in gen_combinations(records):
        #print(f"G {g}")
        cont_seqs = g.replace('.', ' ').split()
        #print(f"CS {cont_seqs} CH {checks}")
        if len(cont_seqs) != len(checks):
            continue
        if any(len(k) != l for k, l in zip(cont_seqs, checks)):
            continue
        print(f"    {g} works")
        n += 1

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