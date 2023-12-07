import math

def ways(t: int, d: int) -> int:
    # solve quadratic (t - p) * p > d for p
    # first find root of tp - p^2 - d = 0
    # then take region between roots

    delta = (t * t - 4 * d)

    # distance greater than max achieveable (t^2/4)
    if delta < 0:
        return 0

    sqrt_delta = math.sqrt(delta)

    r1 = (t + sqrt_delta) / 2
    r2 = (t - sqrt_delta) / 2
    w = math.ceil(r1) - math.floor(r2) - 1
    #print(f"d: {d} t: {t} w: {w} range: {r2}-{r1}")
    return w

def main():
    times = [int(v) for v in input().removeprefix("Time:").strip().split()]
    distances = [int(v) for v in input().removeprefix("Distance:").strip().split()]

    product = 1
    for t, d in zip(times, distances):
        product *= ways(t, d)
    print("PRODUCT", product)

if __name__ == "__main__":
    main()