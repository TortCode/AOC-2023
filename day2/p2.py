import sys
from collections import defaultdict

def parse_set(set: str) -> dict:
    vals = defaultdict(int) 
    for cubes in set.split(','):
        [num, color] = cubes.strip().split(' ')
        vals[color.strip()] = int(num)
    return vals

def getmaxvals(sets: list) -> dict:
    maxvals = {}
    for prop in ['red', 'green', 'blue']:
        maxvals[prop] = max((set[prop] for set in sets), default=0)
    return maxvals

def getpower(line: str) -> int:
    [_, sets] = line.split(':')
    sets = list(map(parse_set, sets.split(';')))
    maxvals = getmaxvals(sets)
    return maxvals['red'] * maxvals['green'] * maxvals['blue'] 

if __name__ == "__main__":
    print(sum(getpower(line) for line in sys.stdin))