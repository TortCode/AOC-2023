from itertools import islice
from collections import namedtuple
import sys

# polyfill for batched???
def batched(iterable, n):
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch

class Range(namedtuple('Range', ['start', 'end'])):
    __slots__ = ()
    
    def __and__(self, other: 'Range'):
        """intersection"""
        start = max(self.start, other.start)
        end = min(self.end, other.end)
        return Range(start, end)

    def __sub__(self, other: 'Range'):
        """assymetric difference"""
        left_split = Range(self.start, other.start-1)
        right_split = Range(other.end+1, self.end)
        return left_split, right_split
    
    def __rshift__(self, v: int):
        return Range(self.start + v, self.end + v)
    
    @property
    def empty(self):
        """is range empty"""
        return self.start > self.end
    
    @property
    def length(self):
        return self.end - self.start + 1

    def __repr__(self) -> str:
        return f"(size {self.length})[{self.start}, {self.end}]"
    
def get_seeds() -> set[Range]:
    for line in sys.stdin:
        if line.startswith("seeds:"):
            line = line.removeprefix("seeds:").strip()
            vals = [int(v) for v in line.split()]
            ranges = set(Range(s, s+l-1) for (s, l) in batched(vals, n=2))
            return ranges

def transform(inputs: set[Range], mapping_name: str) -> set[Range]:
    outputs = set() 

    # get to right line for table
    for line in sys.stdin:
        if line.startswith(mapping_name):
            break
    
    # process each line
    for line in sys.stdin:
        line = line.strip()
        if len(line) == 0:
            break
        [dest, src, length] = [int(v) for v in line.split()]
        r = Range(src, src+length-1)
        for x in inputs.copy():
            overlap = x & r
            if overlap.empty:
                continue

            # remove the overlap from x
            # reinsert non-overlapping part as needed
            inputs.remove(x)
            lsplit, rsplit = x - overlap
            if not lsplit.empty:
                inputs.add(lsplit)
            if not rsplit.empty:
                inputs.add(rsplit)

            # add shifted part to outputs
            outputs.add(overlap >> (dest - src))

    outputs.update(inputs)
    return outputs

def print_list(L):
    for x in L:
        print(x)

def main():
    seeds = get_seeds()
    print("SEEDS")
    print_list(seeds)

    soils = transform(seeds, "seed-to-soil")
    print("SOILS")
    print_list(soils)

    fertilizers = transform(soils, "soil-to-fertilizer")
    print("FERTILIZERS")
    print_list(fertilizers)

    waters = transform(fertilizers, "fertilizer-to-water")
    print("WATERS")
    print_list(waters)

    lights = transform(waters, "water-to-light")
    print("LIGHTS")
    print_list(lights)

    temperatures = transform(lights, "light-to-temperature")
    print("TEMPERATURES")
    print_list(temperatures)
    
    humidities = transform(temperatures, "temperature-to-humidity")
    print("HUMIDITIES")
    print_list(humidities)

    locations = transform(humidities, "humidity-to-location")
    print("LOCATIONS")
    print_list(locations)

    print("LOWEST LOCATION", min(x.start for x in locations))

if __name__ == "__main__":
    main()