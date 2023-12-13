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

def find_row(g):
    R = len(g)
    C = len(g[0])
    for i in range(1, R):
        s = i - 1
        t = i
        good = True
        while good and s >= 0 and t < R:
            if any(g[s][j] != g[t][j] for j in range(C)):
                good = False
            s -= 1
            t += 1
        if good:
            return i

    return 0

def find_column(g):
    R = len(g)
    C = len(g[0])
    for j in range(1, C):
        s = j - 1
        t = j
        good = True
        while good and s >= 0 and t < C:
            if any(g[i][s] != g[i][t] for i in range(R)):
                good = False
            s -= 1
            t += 1
        if good:
            return j

    return 0

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