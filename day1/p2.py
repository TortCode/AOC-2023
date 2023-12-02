import sys

digit_map = {
    **{str(i): i for i in range(10)},
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def get_digit(line: str, pos: str) -> int:
    finder = line.find if pos == 'first' else line.rfind
    cmp = (lambda x, y: x < y) if pos == 'first' else (lambda x, y: x > y)
    cur_idx = -1
    cur_val = 0
    for k, v in digit_map.items():
        idx = finder(k)
        if idx == -1:
            continue
        if cur_idx == -1 or cmp(idx, cur_idx):
            cur_idx = idx
            cur_val = v
    return cur_val

def parse_calibration(line: str):
    return 10 * get_digit(line, 'first') + get_digit(line, 'last')

if __name__ == '__main__':
    print(sum(map(parse_calibration, sys.stdin)))