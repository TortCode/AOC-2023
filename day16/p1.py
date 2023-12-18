import sys
from collections import deque

class Solver:
    def __init__(self, inp: list[str]):
        self.grid = inp
        self.visited = set()
        self.energized = set()

    def find_energized(self):
        self.bfs((0, 0), (0, 1))
        return self.energized

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
    eg = sv.find_energized()
    print(f"ENERGIZED {len(eg)}")

if __name__ == "__main__":
    main()