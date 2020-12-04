#!/usr/bin/env python3
import re


def parse_policy():
    rex = re.compile(r"(\d+)-(\d+)\s([a-z])")
    with open("input") as f:
        for line in f.readlines():
            policy, pw = line.strip().split(": ")
            lower_bound, upper_bound, char = rex.search(policy).groups()
            yield int(lower_bound), int(upper_bound), char, pw


def solution():
    part1, part2 = 0, 0
    for a, b, char, pw in parse_policy():
        if a <= pw.count(char) <= b:
            part1 += 1

        if (pw[a-1] == char) ^ (pw[b-1] == char):
            part2 += 1

    return part1, part2


ans1, ans2 = solution()
print(f"part1: {ans1}")  # 398
print(f"part2: {ans2}")  # 562
