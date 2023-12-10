from collections import namedtuple, deque
import sys

PipeConn = namedtuple('PipeConn', ['N', 'E', 'S', 'W'])

class Grid:
    OFFSETS = [
        (-1, 0), #NORTH
        (0, 1),  #EAST
        (1, 0),  #SOUTH
        (0, -1)  #WEST
    ]

    def __init__(self, lines: list[str]):
        self.nrows = len(lines)
        self.ncols = len(lines[0])
        self.pipes = [[Grid.process_char(c) for c in line] for line in lines]
        self.start = Grid.find_start(lines)

    def in_range(self, i, j):
        return 0 <= i < self.nrows and 0 <= j < self.ncols

    @staticmethod
    def find_start(lines: list[str]):
        for i, line in enumerate(lines):
            if line.count('S') > 0:
                return (i, line.index('S'))
        raise LookupError("Could not find start")

    @staticmethod
    def process_char(c):
        N = E = S = W = False
        match c:
            case '|':
                N = S = True
            case '-':
                E = W = True
            case 'L':
                N = E = True
            case 'J':
                N = W = True
            case '7':
                S = W = True
            case 'F':
                S = E = True
            case '.':
                pass
            case 'S':
                N = E = S = W = True
        return PipeConn(N, E, S, W)

    def __repr__(self) -> str:
        s = ""
        for line in self.pipes:
            for pipe in line:
                part = [' '] * 4 
                if pipe.N:
                    part[0] = '^'
                if pipe.E:
                    part[1] = '>'
                if pipe.S:
                    part[2] = 'v'
                if pipe.W:
                    part[3] = '<'
                s += ''.join(part) + '|'
            s += '\n'
        return s

    def farthest(self) -> int:
        d = 0
        visited = [[False] * self.ncols for _ in range(self.nrows)]
        q = deque() 
        q.append(self.start)
        while q:
            #print(q, d)
            N = len(q)
            for _ in range(N):
                i, j = q.popleft()
                visited[i][j] = True
                for dir, (di, dj) in enumerate(Grid.OFFSETS):
                    ni = i + di
                    nj = j + dj
                    if not self.in_range(ni, nj) or visited[ni][nj]:
                        continue
                    if self.pipes[i][j][dir] and self.pipes[ni][nj][(dir + 2) % 4]:
                        q.append((ni, nj))
            d += 1
        return d - 1


def main():
    lines = [line.strip() for line in sys.stdin.readlines()]
    grid = Grid(lines)
    # print("GRID:")
    # print(grid)
    print("FARDIST:")
    print(grid.farthest())

if __name__ == "__main__":
    main()
