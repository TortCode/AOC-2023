import sys
import math

class Stepper:
    node_map = {}
    lrs = []
    lr_len = 0

    def __init__(self, node: str, pos: int = 0, idx: int = 0):
        self.node = node
        self.pos = pos
        self.lr_idx = idx 

    def advance(self, times=1):
        for _ in range(times):
            self.node = self.node_map[self.node][self.lrs[self.lr_idx]]
            self.lr_idx = (self.lr_idx + 1) % self.lr_len
            self.pos += 1
        return self

    def clone(self):
        return Stepper(self.node, self.pos, self.lr_idx)

    def __eq__(self, other: 'Stepper') -> bool:
        return self.node == other.node and self.lr_idx == other.lr_idx
    
    def __repr__(self) -> str:
        return f"{self.node} @ letter {self.lr_idx}"

class CRTSolver:
    def __init__(self):
        self.residues = []
        self.moduli = []
        self.bad = False

    def add_equation(self, res: int, mod: int):
        if self.bad:
            return
        N = len(self.moduli)
        for i in range(N):
            r = self.residues[i]
            m = self.moduli[i]
            if (g := math.gcd(m, mod)) != 1:
                # ensure still proper
                if res % g != r % g:
                    self.bad = True
                    return
                self.residues.append(r % g)
                self.moduli.append(g)
                # split up equations
                m //= g
                r %= m
                self.moduli[i] = m
                self.residues[i] = r 
                mod //= g
                res %= mod
        self.residues.append(res)
        self.moduli.append(mod)

    @staticmethod
    def inverse(x, m):
        M = m
        sx, tx = 1, 0
        sm, tm = 0, 1
        while x != 0:
            k = m // x
            x, m = m - k * x, x
            sx, sm = sm - k * sx, sx
            tx, tm = tm - k * tx, tx
            #print(sx, tx, sm, tm)
        return (sm % M + M) % M

    def solve(self) -> tuple[int, int]:
        if self.bad:
            return False
        M = 1
        for m in self.moduli:
            M *= m

        x = 0
        for r, m in zip(self.residues, self.moduli):
            x += r * (M // m) * CRTSolver.inverse((M // m) % m, m)
        return x % M, M

def get_node_map(fp):
    node_map = {}
    for line in fp:
        line = line.strip()
        if len(line) == 0:
            continue
        [src, dests] = [v.strip() for v in line.split("=")]
        [dest_left, dest_right] = [v.strip() for v in dests.lstrip('(').rstrip(')').split(',')]
        node_map[src] = dest_left, dest_right
    return node_map

def cycle_find(x0: str, lrs: str, node_map: dict):
    slow = Stepper(x0).advance()
    fast = Stepper(x0).advance(2)

    #find k * length 
    while slow != fast:
        slow.advance()
        fast.advance(2)
    
    # find start
    fast = Stepper(x0)
    start = 0
    while slow != fast:
        slow.advance()
        fast.advance()
        start += 1

    # find length
    slow = fast.clone()
    fast.advance()
    while slow != fast:
        fast.advance()
    return start, fast.pos - slow.pos

def generate_multi_indices(return_list, matrix, idx=0, cur_list=None):
    if cur_list is None:
        cur_list = []
    if idx == len(matrix):
        return_list.append(cur_list[:]) 
        return
    for v in matrix[idx]:
        cur_list.append(v)
        generate_multi_indices(return_list, matrix, idx + 1, cur_list)
        cur_list.pop()

def solve(fp):
    lr_list = [0 if c == 'L' else 1 for c in fp.readline().strip()]
    LR_LEN = len(lr_list)
    node_map = get_node_map(fp)
    Stepper.lrs = lr_list
    Stepper.node_map = node_map
    Stepper.lr_len = LR_LEN

    src_nodes = [n for n in node_map.keys() if n[-1] == "A"]
    starts = []
    mods = []
    z_nodes_matrix = []
    for n in src_nodes:
        s, l = cycle_find(n, lr_list, node_map)
        starts.append(s)
        mods.append(l)
        print(f"node {n}: cycle @ {s} ({l})")
        stepper = Stepper(n).advance(s)
        z_nodes = []
        for _ in range(l):
            if stepper.node[-1] == 'Z':
                z_nodes.append(stepper.pos)
                print(f"position {stepper.pos} : {Stepper(n).advance(stepper.pos)}")
            stepper.advance()
        z_nodes_matrix.append(z_nodes)

    max_start = max(starts)

    multi_indices = []
    generate_multi_indices(multi_indices, z_nodes_matrix)

    min_steps = float("inf")
    for multi_index in multi_indices:
        crt = CRTSolver()
        print("SYSTEM")
        for v, m in zip(multi_index, mods):
            print(f"\tx = {v} mod {m}")
            crt.add_equation(v, m)
        v, m = crt.solve()
        print(f"SOLUTION")
        print(f"\tx = {v} mod {m}")
        steps = max_start + (v - (max_start % m) + m) % m
        print(f"STEPS {steps}")
        min_steps = min(min_steps, steps)
    
    print(f"MIN STEPS {min_steps}")


if __name__ == "__main__":
    fp = open(sys.argv[1], 'r') if len(sys.argv) >= 2 else sys.stdin
    solve(fp)