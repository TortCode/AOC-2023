import sys

def parse_calibration(line: str):
    digits = list(filter(str.isdigit, line))
    x = int(digits[0] + digits[-1])
    return x

if __name__ == '__main__':
    print(sum(map(parse_calibration, sys.stdin)))