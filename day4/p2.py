import sys
from collections import defaultdict

def num_matches(line: str) -> int:
    line = line.split(':')[1]
    parts = line.split('|')
    assert len(parts) == 2
    win_nos = set(parts[0].split())
    card_nos = set(parts[1].split())
    common = len(win_nos & card_nos)
    return common

def main():
    num_cards = defaultdict(int)
    for i, line in enumerate(sys.stdin):
        num_cards[i] += 1
        M = num_matches(line)
        for j in range(i+1, i+1+M):
            num_cards[j] += num_cards[i]
    print(sum(num_cards.values()))

if __name__ == "__main__":
    main()