import sys

def cross(a, b):
    ax, ay = a
    bx, by = b
    return ax * by - ay * bx

def main():
    inp = get_input()
    area = 0
    boundary = 0
    prev_pos = 0,0
    pos = 0,0
    for d, l in inp:
        boundary += l
        match d:
            case 'R':
                pos = pos[0] + l, pos[1]
            case 'L':
                pos = pos[0] - l, pos[1]
            case 'U':
                pos = pos[0], pos[1] + l
            case 'D':
                pos = pos[0], pos[1] - l
        area += cross(prev_pos, pos) / 2
        prev_pos = pos

    area = abs(area)
    interior = int(area + 1 - boundary / 2)
    print(f"ALL {interior + boundary}")


def get_input():
    inp = []
    for line in sys.stdin:
        [_, _, hex] = line.strip().split()
        hex = hex.strip('()#')
        l = int(hex[:5], 16)
        match int(hex[5]):
            case 0:
                d = 'R'
            case 1:
                d = 'D'
            case 2:
                d = 'L'
            case 3:
                d = 'U'
        inp.append((d, l))
    return inp
if __name__ == "__main__":
    main()