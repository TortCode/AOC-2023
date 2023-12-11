
import sys

class GalaxyGrid:
    EXPANSION_FACTOR = 10 ** 6
    def __init__(self, lines: list[str]):
        self.grid: list[str] = lines
        self.row_expansion()
        self.col_expansion()
        self.find_galaxies()

    def row_expansion(self):
        self.row_expand = [line.count('#') == 0 for line in self.grid]

    def col_expansion(self):
        self.col_expand = [[self.grid[j][i] for j in range(len(self.grid))].count('#') == 0 for i in range(len(self.grid[0]))]

    def find_galaxies(self):
        self.galaxies = []
        for i, line in enumerate(self.grid):
            for j, c in enumerate(line):
                if c == '#':
                    self.galaxies.append((i, j))
    
    def distance_between(self, g1, g2):
        i1, j1 = g1
        i2, j2 = g2
        di = abs(i2 - i1)
        dj = abs(j2 - j1)
        mi = min(i1, i2)
        Mi = max(i1, i2)
        mj = min(j1, j2)
        Mj = max(j1, j2)
        expanded_rows = self.row_expand[mi:Mi+1].count(True)
        expanded_cols = self.col_expand[mj:Mj+1].count(True)

        return di + dj + (expanded_rows + expanded_cols) * (GalaxyGrid.EXPANSION_FACTOR - 1)
    

def main():
    lines = [line.strip() for line in sys.stdin.readlines()]

    length_sum = 0
    gg = GalaxyGrid(lines)
    for i in range(len(gg.galaxies)):
        for j in range(i+1, len(gg.galaxies)):
            length_sum += gg.distance_between(gg.galaxies[i], gg.galaxies[j])

    print(f"SUM {length_sum}")

if __name__ == "__main__":
    main()