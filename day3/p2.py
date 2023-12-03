import sys
from collections import defaultdict

def is_symbol(c):
    return c != '.' and not c.isdigit()

def main():
    gear_ratio_sum = 0
    grid = list(map(str.strip, sys.stdin.readlines()))
    gear_map = defaultdict(list)

    def get_next_number(i: int, j: int) -> (str):
        number = "" 
        oldj = j
        while j < len(grid[0]) and grid[i][j].isdigit():
            number = number + grid[i][j]
            j += 1
        if len(number) == 0:
            return ""
        neighbours = get_symbol_neighbours(i, oldj, len(number))
        for i, j in neighbours:
            gear_map[(i, j)].append(number)
        return number

    def get_symbol_neighbours(i: int, j: int, length: int) -> list[(int, int)]:
        ans = []
        offsets = [(-1, dj) for dj in range(-1, length+1)] + [(1, dj) for dj in range(-1, length+1)] + [(0, -1), (0, length)]
        for di, dj in offsets:
            ni = i + di
            nj = j + dj
            #print("\tVISIT", ni, nj)
            if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and is_symbol(grid[ni][nj]):
                ans.append((ni, nj))
        return ans

    print("BUILDING GEAR MAP")
    for i, row in enumerate(grid):
        print("ROW", i)
        j = 0
        while j < len(row):
            #print("\tCOL", j)
            number = get_next_number(i, j)
            #if len(number) > 0:
                #print("\tNUM", number)
                #print("\tGEAR MAP", dict(gear_map))
            j += max(len(number), 1)
    print("CALCULATING GEAR RATIOS")
    for _, numbers in gear_map.items():
        if len(numbers) == 2:
            gear_ratio_sum += int(numbers[0]) * int(numbers[1])
    print("SUM", gear_ratio_sum)

if __name__ == "__main__":
    main()