import sys
from collections import deque

class Solver:
    def __init__(self, inp: list[str]):
        self.grid = inp
        self.visited = set()
        self.energized = set()

    def count_energized(self, pos, dir):
        print(f"p: {pos} -> {dir}")
        self.visited.clear()
        self.energized.clear()
        self.bfs(pos, dir)
        return len(self.energized)
    
    def max_energized(self):
        R = len(self.grid)
        C = len(self.grid[0])
        max_e = 0
        for i in range(R):
            max_e = max(max_e, self.count_energized((0, i), (1, 0)))
        for i in range(R):
            max_e = max(max_e, self.count_energized((R-1, i), (-1, 0)))
        for j in range(C):
            max_e = max(max_e, self.count_energized((j, 0), (0, 1)))
        for j in range(C):
            max_e = max(max_e, self.count_energized((j, C-1), (0, -1)))

        return max_e

    def is_valid(self, pos: tuple[int, int]):
        r, c = pos
        return 0 <= r < len(self.grid) and 0 <= c < len(self.grid[0]) 

    @staticmethod
    def new_dirs(comp: str, dir: tuple[int, int]):
        dr, dc = dir
        match comp:
            case '.':
                return [dir]
            case '|':
                return [dir] if dr != 0 else [(-1, 0), (1, 0)]
            case '-':
                return [dir] if dc != 0 else [(0, -1), (0, 1)]
            case '\\':
                return [(dc, dr)]
            case '/':
                return [(-dc, -dr)]
        raise ValueError()

    def bfs(self, pos: tuple[int, int], dir: tuple[int, int]):
        q = deque()
        q.append((pos, dir))
        while q:
            pos, dir = q.popleft()
            if not self.is_valid(pos):
                continue
            if (pos, dir) in self.visited:
                continue
            self.visited.add((pos, dir))

            r, c = pos
            self.energized.add((r, c))
            for dr, dc in Solver.new_dirs(self.grid[r][c], dir):
                q.append(((r + dr, c + dc), (dr, dc)))

def main():
    inp = [line.strip() for line in sys.stdin]
    sv = Solver(inp)
    eg = sv.max_energized()
    print(f"ENERGIZED {eg}")

if __name__ == "__main__":
    main()