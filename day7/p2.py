import sys
from collections import defaultdict

def parse_line(line: str) -> (str, int):
    [hand, bid] = line.strip().split()
    return hand, int(bid)

def type_rank(hand: str) -> int:
    """smaller value is stronger"""
    freq_dict = defaultdict(int)
    for c in hand:
        freq_dict[c] += 1
    j = freq_dict['J']
    freq_dict['J'] = 0

    freqs = sorted(freq_dict.values(), reverse=True)
    freqs[0] += j
    #print("FREQS", freqs)

    match freqs[0]:
        case 5:
            return 0
        case 4:
            return 1
        case 3:
            return 2 if freqs[1] == 2 else 3
        case 2:
            return 4 if freqs[1] == 2 else 5
        case 1:
            return 6

ordering = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
def lex_order(hand: str):
    """lexicographically smaller value is stronger"""
    output = ""
    for c in hand:
        output += chr(ord('a') + ordering.index(c))
    return output

def get_key(hand: str):
    t = type_rank(hand)
    lex = lex_order(hand)
    #print(f"{hand} -> {lex}:{t}")
    return t, lex

def main():
    inputs = [parse_line(line) for line in sys.stdin]
    inputs.sort(key=lambda play: get_key(play[0]), reverse=True)

    winnings = 0
    for i, (h, b) in enumerate(inputs):
        #print(f"HAND: {h} RANK: {i+1} BID: {b}")
        winnings += (i + 1) * b
    print("WINNINGS", winnings)

if __name__ == "__main__":
    main()