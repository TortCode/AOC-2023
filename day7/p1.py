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
    
    freqs = list(freq_dict.values())

    # five of kind
    if 5 in freqs:
        return 0
    # four of kind
    if 4 in freqs:
        return 1
    if 3 in freqs:
        # full house
        if 2 in freqs:
            return 2 
        # three of kind
        else:
            return 3
    pair_count = freqs.count(2)
    # two pairs
    if pair_count == 2:
        return 4
    # one pair
    if pair_count == 1:
        return 5
    
    # only case left is high card
    return 6

ordering = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
def lex_order(hand: str):
    """lexicographically smaller value is stronger"""
    output = ""
    for c in hand:
        output += chr(ord('a') + ordering.index(c))
    return output

def get_key(hand: str):
    t = type_rank(hand)
    lex = lex_order(hand)
    print(f"{hand} -> {lex}:{t}")
    return t, lex

def main():
    inputs = [parse_line(line) for line in sys.stdin]
    inputs.sort(key=lambda play: get_key(play[0]), reverse=True)

    winnings = 0
    for i, (h, b) in enumerate(inputs):
        print(f"HAND: {h} RANK: {i+1} BID: {b}")
        winnings += (i + 1) * b
    print("WINNINGS", winnings)

if __name__ == "__main__":
    main()