import sys

def main():
    grid = read_input()
    total_load = 0
    for column in transpose(grid):
        next_load = len(column)
        for i, rock in enumerate(column, start=1):
            match rock:
                case 'O':
                    total_load += next_load
                    next_load -= 1
                case '#':
                    next_load = len(column) - i
                case '.':
                    pass
    print(f"LOAD {total_load}")
    

def read_input():
    grid = [line.strip() for line in sys.stdin]
    return grid

def transpose(g):
    return ["".join([g[i][j] for i in range(len(g))])for j in range(len(g[0]))]

if __name__ == "__main__":
    main()