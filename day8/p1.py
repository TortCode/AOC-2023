import sys
from itertools import cycle

def main():
    lr_list = sys.stdin.readline().strip()
    print(lr_list)
    node_map = {}
    for line in sys.stdin:
        line = line.strip()
        if len(line) == 0:
            continue
        [src, dests] = [v.strip() for v in line.split("=")]
        [dest_left, dest_right] = [v.strip() for v in dests.lstrip('(').rstrip(')').split(',')]
        node_map[src] = dest_left, dest_right

    cur_node = "AAA"
    nsteps = 0
    for c in cycle(lr_list):
        match c:
            case 'L':
                cur_node = node_map[cur_node][0]
            case 'R':
                cur_node = node_map[cur_node][1]
        nsteps += 1
        print(f"{nsteps}: {c} -> {cur_node}")
        if cur_node == "ZZZ":
            break
    print("STEPS", nsteps)
    

if __name__ == "__main__":
    main()