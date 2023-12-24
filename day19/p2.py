import sys
from collections import namedtuple, deque

Rule = namedtuple('Rule', ['key', 'val', 'op', 'dest'])

class MultiRange(namedtuple('MultiRange', ['x', 'm', 'a', 's'])):
    @staticmethod
    def start():
        m = 1
        M = 4000
        return MultiRange(Range(m, M), Range(m, M), Range(m, M), Range(m, M))

    def split_on(self, key, val, op):
        if op is None:
            return self, None
        match op:
            case '<':
                tpart, fpart = getattr(self, key) < val
            case '>':
                tpart, fpart = getattr(self, key) > val

        t = self._replace(**{key: tpart})
        f = self._replace(**{key: fpart})
        return t, f

    def combinations(self):
        return len(self.x) * len(self.m) * len(self.a) * len(self.s)
        
class Range(namedtuple('Range', ['lo', 'hi'])):
    def __gt__(self, val):
        lo = max(self.lo, val + 1)
        # true, false pair
        return Range(lo, self.hi), Range(self.lo, lo - 1)
    def __lt__(self, val):
        hi = min(self.hi, val - 1)
        # true, false pair
        return Range(self.lo, hi), Range(hi + 1, self.hi)
    def __len__(self):
        return max(self.hi - self.lo + 1, 0)

def main():
    workflows = get_input()
    print(workflows)

    rating_sum = 0
    q = deque([(MultiRange.start(), 'in')])

    while q:
        mr, current = q.popleft()
        if current == 'A':
            print("accepted", mr)
            rating_sum += mr.combinations()
            continue
        if current == 'R':
            print("rejected", mr)
            continue
        for rule in workflows[current]:
            if mr is None or len(mr) == 0:
                break
            t, f = mr.split_on(rule.key, rule.val, rule.op)
            mr = f
            q.append((t, rule.dest))

    print(rating_sum)

def get_input():
    workflows = {}
    for line in sys.stdin:
        rules = []
        line = line.strip()
        if len(line) == 0:
            break
        name, right = line.split('{')
        unparsed_rules = right.rstrip('}').split(',')
        for r in unparsed_rules:
            if ':' in r:
                [cond, dest] = r.split(':')
                if '<' in cond:
                    attr, val = cond.split('<')
                    rule = Rule(attr, int(val), '<', dest)
                elif '>' in cond:
                    attr, val = cond.split('>')
                    rule = Rule(attr, int(val), '>', dest)
            else:
                rule = Rule(None, None, None, r)
            rules.append(rule)
        workflows[name] = rules

    return workflows

if __name__ == "__main__":
    main()