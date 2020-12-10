#!/usr/bin/env python3
from itertools import combinations as combo


def parse_adapters(input_file):
    with open(input_file) as f:
        return sorted([int(line) for line in f.readlines()])


def part1(adapters):
    joltage, ones = 0, 0
    threes = 1
    for adapter in adapters:
        if (diff := adapter - joltage) == 3:
            threes += 1
        elif diff == 1:
            ones += 1
        joltage = adapter
    return ones * threes


def part2(adapters):
    def multiplier(adpts, low, high):
        lst = []
        for i in range(1, 4):
            lst += [ele for ele in combo(adpts, i) if high - max(ele) <= 3]
        return len(lst) + sum((1 for ele in lst if min(ele) - low <= 3))

    arrangements = 1
    joltage = 0
    lo = float("-INF")
    adpts = []

    for adapter in adapters:
        if adapter - joltage > 3:
            joltage = adapter
            arrangements *= multiplier(adpts, lo, adapter)
            lo = adpts[-1]
            adpts.clear()
        else:
            adpts.append(adapter)

    if adpts:
        arrangements *= multiplier(adpts, lo, max(adpts) + 3)

    return arrangements


def main():
    parsed = parse_adapters("input")
    print(f"part1: {part1(parsed)}")  # 2590
    print(f"part2: {part2(parsed)}")  # 226775649501184


if __name__ == "__main__":
    main()
