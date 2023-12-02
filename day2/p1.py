import sys

def parse_set(set: str) -> dict:
    vals = {}
    for cubes in set.split(','):
        [num, color] = cubes.strip().split(' ')
        vals[color.strip()] = int(num)
    return vals

def is_valid(sets) -> bool:
    for set in sets:
        if 'red' in set and set['red'] > 12:
            return False
        if 'green' in set and set['green'] > 13:
            return False
        if 'blue' in set and set['blue'] > 14:
            return False
    return True

def getid(line: str) -> int:
    [gameinfo, sets] = line.split(':')
    id = int(gameinfo.split('Game')[1])
    sets = map(parse_set, sets.split(';'))
    return id if is_valid(sets) else 0

if __name__ == "__main__":
    print(sum(getid(line) for line in sys.stdin))