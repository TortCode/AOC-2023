import sys

def card_points(line: str) -> int:
    line = line.split(':')[1]
    parts = line.split('|')
    assert len(parts) == 2
    win_nos = set(parts[0].split())
    card_nos = set(parts[1].split())
    common = len(win_nos & card_nos)
    return 0 if common == 0 else 2 ** (common - 1)

def main():
    print(sum(card_points(line) for line in sys.stdin))

if __name__ == "__main__":
    main()