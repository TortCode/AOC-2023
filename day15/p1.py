import sys

def main():
    line = sys.stdin.readline()
    strings = line.strip().split(',')
    s = sum(hash(string) for string in strings)
    print(f"SUM {s}")

def hash(string: str):
    v = 0
    for c in string:
        v += ord(c)
        v *= 17
        v &= 0xFF 
    print(f"hash({string}) = {v}")
    return v

if __name__ == "__main__":
    main()