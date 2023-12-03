import sys

def is_symbol(c):
    return c != '.' and not c.isdigit()

def has_symbol_neighbour(grid: list[str], i: int, j: int) -> bool:
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if di == 0 and dj == 0:
                continue
            ni = i + di
            nj = j + dj
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and is_symbol(grid[ni][nj]):
                return True
    return False

def get_next_number(grid: list[str], i: int, j: int) -> (str, bool):
    is_part_number = False
    number = "" 
    while j < len(grid[0]) and grid[i][j].isdigit():
        number = number + grid[i][j]
        if not is_part_number and has_symbol_neighbour(grid, i, j):
            is_part_number = True
        j += 1
    return number, is_part_number

def main():
    part_sum = 0
    grid = list(map(str.strip, sys.stdin.readlines()))
    for i, row in enumerate(grid):
        print("ROW", i)
        j = 0
        while j < len(row):
            #print("\tCOL", j)
            number, is_part = get_next_number(grid, i, j)
            if is_part:
                part_sum += int(number)
                #print("NUM", number)
            j += max(len(number), 1)
    print("SUM", part_sum)

if __name__ == "__main__":
    main()