import sys
from heapq import *

DIR_OFFSETS = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

def main():
    grid = [[int(c) for c in line.strip()] for line in sys.stdin]
    R = len(grid)
    C = len(grid[0])

    def in_range(i, j):
        return 0 <= i < R and 0 <= j < C
    # dims: row x column x dir x len of path in dir
    INF = float('inf')
    loss = [[[[INF] * 10 for _ in range(4)] for _ in range(C)] for _ in range(R)]
    visited = [[[[False] * 10 for _ in range(4)] for _ in range(C)] for _ in range(R)]
    loss[0][1][0][0] = 0
    loss[1][0][1][0] = 0

    heap = [(0, 0, 1, 0, 0), (0, 1, 0, 1, 0)]

    while len(heap) > 0:
        l, i, j, d, c = heappop(heap)
        #print(f"PATH L: {l} ({i}, {j}) -> {DIR_OFFSETS[d]} {c}")
        if visited[i][j][d][c]:
            continue
        visited[i][j][d][c] = True
        if c >= 3:
            for nd in [d-1, d+1]:
                nd += 4
                nd %= 4
                di, dj = DIR_OFFSETS[nd]
                ni, nj = i + di, j + dj
                if not in_range(ni, nj):
                    continue
                if l + grid[i][j] < loss[ni][nj][nd][0]:
                    loss[ni][nj][nd][0] = nl = l + grid[i][j]
                    heappush(heap, (nl, ni, nj, nd, 0))
        if c < 9:
            di, dj = DIR_OFFSETS[d]
            ni, nj = i + di, j + dj
            if not in_range(ni, nj):
                continue
            if l + grid[i][j] < loss[ni][nj][d][c+1]:
                loss[ni][nj][d][c+1] = nl = l + grid[i][j]
                heappush(heap, (nl, ni, nj, d, c+1))

    dist = min(min(sub[3:]) for sub in loss[R-1][C-1]) + grid[R-1][C-1]
    print(f"DIST {dist}")

if __name__ == "__main__":
    main()