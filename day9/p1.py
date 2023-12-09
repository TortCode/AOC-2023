import sys

def extrapolate(vals: list[int]) -> int:
    matrix = [vals]
    diffs = vals
    while diffs.count(0) != len(diffs):
        diffs = [t - s for s, t in zip(diffs, diffs[1:])]
        matrix.append(diffs)
    
    return sum(hist[-1] for hist in matrix)

def main():
    sum = 0
    for line in sys.stdin:
        seq = [int(v) for v in line.strip().split()]
        ext = extrapolate(seq)
        sum += ext
        print(seq, ext)
    print(f"SUM {sum}")


if __name__ == "__main__":
    main()