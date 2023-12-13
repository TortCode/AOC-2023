import sys

def get_grids():
    lines = [line.strip() for line in sys.stdin.readlines()]
    grids = []
    cur_grid = []
    for line in lines:
        if len(line) == 0:
            grids.append(cur_grid)
            cur_grid = []
        else:
            cur_grid.append(line)
    if len(cur_grid) > 0:
        grids.append(cur_grid)

    return grids

def transpose(g):
    return ["".join([g[i][j] for i in range(len(g))])for j in range(len(g[0]))]

def find_row(g):
    R = len(g)
    C = len(g[0])
    for i in range(1, R):
        s = i - 1
        t = i
        changes = 0
        while changes <= 1 and s >= 0 and t < R:
            off = list(j for j in range(C) if g[s][j] != g[t][j])
            changes += len(off)
            s -= 1
            t += 1
        if changes == 1:
            return i

    return 0

def find_column(g):
    return find_row(transpose(g))

def main():
    grids = get_grids()

    s = 0
    for i, g in enumerate(grids):
        print(f"GRID {i}:")
        # for r in g:
        #     print(r)
        # print()
        reflection_col = find_column(g)
        reflection_row = find_row(g)
        print(f"R {reflection_row} C {reflection_col}")
        s += reflection_row * 100 + reflection_col

    print(f"SUM {s}")


if __name__ == '__main__':
    main()