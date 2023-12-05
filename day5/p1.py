import sys

def get_seeds() -> [int]:
    for line in sys.stdin:
        if line.startswith("seeds:"):
            line = line.removeprefix("seeds:").strip()
            return [int(v) for v in line.split()]

def transform(inputs: [int], mapping_name: str) -> [int]:
    outputs = inputs[:]
    for line in sys.stdin:
        if line.startswith(mapping_name):
            break
    for line in sys.stdin:
        line = line.strip()
        if len(line) == 0:
            break
        [dest, src, length] = [int(v) for v in line.split()]
        for i, x in enumerate(inputs):
            if src <= x < src + length:
                outputs[i] = dest + (x - src)
    return outputs

def main():
    seeds = get_seeds()
    print("SEEDS", seeds)
    soils = transform(seeds, "seed-to-soil")
    print("SOILS", soils)
    fertilizers = transform(soils, "soil-to-fertilizer")
    print("FERTILIZERS", fertilizers)
    waters = transform(fertilizers, "fertilizer-to-water")
    print("WATERS", waters)
    lights = transform(waters, "water-to-light")
    print("LIGHTS", lights)
    temperatures = transform(lights, "light-to-temperature")
    print("TEMPERATURES", temperatures)
    humidities = transform(temperatures, "temperature-to-humidity")
    print("HUMIDITIES", humidities)
    locations = transform(humidities, "humidity-to-location")
    print("LOCATIONS", locations)
    print("LOWEST LOCATION", min(locations))

if __name__ == "__main__":
    main()