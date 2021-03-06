#!/usr/bin/env python3
from math import prod

with open("input") as f:
    weird_biome = [line.strip() for line in f.readlines()]


def toboggan(area, slopes):
    wrap = len(area[0])
    for right, down in slopes:
        trees = 0
        shift = right
        for i in range(down, len(area), down):
            if area[i][shift % wrap] == "#":
                trees += 1
            shift += right
        yield trees


p1 = sum(toboggan(weird_biome, [(3, 1)]))
p2 = prod(toboggan(weird_biome, ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))))

print(f"part1: {p1}")  # 195
print(f"part2: {p2}")  # 3772314000
