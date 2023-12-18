
import sys

def main():
    line = sys.stdin.readline()
    boxes = [dict() for _ in range(256)]
    ops = line.strip().split(',')
    for op in ops:
        process_op(boxes, op)
    
    power = focusing_power(boxes)
    print(f"POWER {power}")

def focusing_power(boxes: list[dict[str, int]]):
    p = 0
    for i, box in enumerate(boxes, start=1):
        for j, v in enumerate(box.values(), start=1):
            p += i * j * v
    return p

def process_op(boxes: list[dict[str, int]], op: str):
    label, ch, info = op.partition("=")
    if len(ch) == 0:
        label, ch, info = op.partition('-')

    h = hash(label)
    box = boxes[h]

    match ch:
        case "=":
            box[label] = int(info)
        case "-":
            if label in box:
                del box[label]

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