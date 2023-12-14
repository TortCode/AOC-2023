import sys
from copy import deepcopy

DEBUG_LEVEL = -1 

class Stepper:
    def __init__(self, grid, idx=0):
        self.grid = grid
        self.idx = idx 

    def advance(self, times=1):
        for _ in range(times):
            self.spin_cycle()
            self.idx += 1
        return self

    def clone(self):
        return Stepper(self.grid, self.idx)

    def spin_cycle(self):
        print(f"spin cycle {self.idx + 1}")

        grid = self.grid
        grid = tilt_north(grid)
        if DEBUG_LEVEL >= 0:
            print("north: ")
            print_grid(grid)
        grid = tilt_west(grid)
        if DEBUG_LEVEL >= 0:
            print("west: ")
            print_grid(grid)
        grid = tilt_south(grid)
        if DEBUG_LEVEL >= 0:
            print("south: ")
            print_grid(grid)
        grid = tilt_east(grid)
        if DEBUG_LEVEL >= 0:
            print("east: ")
            print_grid(grid)
        print(f"LOAD {north_load(grid)}")
        self.grid = grid

    def __eq__(self, other: 'Stepper'):
        for x, y in zip(self.grid, other.grid):
            for c, d in zip(x, y):
                if c != d:
                    return False
        return True

def main():
    grid = read_input()
    N = 10 ** 9
    start, length = find_cycle(grid)
    print(f"CYCLE {start}({length})")

    if N < start:
        last_grid = Stepper(grid).advance(N).grid
    else:
        pos = (N - start) % length + start
        last_grid = Stepper(grid).advance(pos).grid
    
    load = north_load(last_grid)
    print(f"FINAL LOAD {load}")

def find_cycle(grid):
    slow = Stepper(grid)
    fast = Stepper(grid)

    # find k * lambda
    while slow.advance() != fast.advance(2):
        pass 

    # find mu
    fast = Stepper(grid)
    while slow != fast:
        slow.advance()
        fast.advance()
    start = fast.idx

    # find lambda
    slow = fast.clone()
    while slow != fast.advance():
        pass

    length = fast.idx - slow.idx
    return start, length

def print_grid(grid):
    for row in grid:
        print("".join(row))

def north_load(grid):
    total_load = 0
    for column in transpose(grid):
        for i, rock in enumerate(column):
            if rock == 'O':
                total_load += len(column) - i
    return total_load
    
def tilt_west(grid):
    copy = deepcopy(grid) 
    for i, row in enumerate(grid):
        next_pos = 0 
        for j, rock in enumerate(row):
            match rock:
                case 'O':
                    if j != next_pos:
                        copy[i][next_pos] = 'O'
                        copy[i][j] = '.'
                    next_pos += 1
                case '#':
                    next_pos = j + 1
                case '.':
                    pass
    if DEBUG_LEVEL >= 1:
        print("tilted: ")
        print_grid(copy)
    return copy

def tilt_east(grid):
    return flipped_rows(tilt_west(flipped_rows(grid)))

def tilt_north(grid):
    return transpose(tilt_west(transpose(grid)))

def tilt_south(grid):
    return transpose(tilt_east(transpose(grid)))

def read_input():
    grid: list[list[str]] = [list(line.strip()) for line in sys.stdin]
    if DEBUG_LEVEL >= 0:
        print("starting: ")
        print_grid(grid)
    return grid

def transpose(g):
    grid = [[g[i][j] for i in range(len(g))] for j in range(len(g[0]))]
    if DEBUG_LEVEL >= 1:
        print("transpose: ")
        print_grid(grid)
    return grid

def flipped_rows(g):
    grid = [list(reversed(row)) for row in g]
    if DEBUG_LEVEL >= 1:
        print("flipped: ")
        print_grid(grid)
    return grid

if __name__ == "__main__":
    main()