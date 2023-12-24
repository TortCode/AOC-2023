import sys
from collections import namedtuple

Part = namedtuple('Part', ['x', 'm', 'a', 's'])
Rule = namedtuple('Rule', ['key', 'val', 'op', 'dest'])

def main():
    workflows, parts = get_input()
    print(workflows)
    print(parts)

    rating_sum = 0

    for part in parts:
        current = 'in'
        while current not in ['A', 'R']:
            for rule in workflows[current]:
                match rule.op:
                    case '<':
                        if getattr(part, rule.key) < rule.val:
                            current = rule.dest
                            break
                    case '>':
                        if getattr(part, rule.key) > rule.val:
                            current = rule.dest
                            break
                    case _:
                        current = rule.dest
                        break
        print(current, part)
        if current == 'A':
            x, m, a, s = part
            rating_sum += x + m + a + s

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
    
    parts = []
    for line in sys.stdin:
        part = {} 
        line = line.strip().lstrip('{').rstrip('}')
        if len(line) == 0:
            break
        kvs = line.split(',')
        for kv in kvs:
            k, v = kv.split('=')
            part[k] = int(v)
        parts.append(Part(**part))

    return workflows, parts

if __name__ == "__main__":
    main()