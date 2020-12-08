#!/usr/bin/env python3
from functools import cache
import re


def parse_rules(input_file):
    bagex = re.compile(r"(\d+) ([\w ]+?) bag")
    rules = {}
    with open(input_file) as f:
        for k, v in map(lambda x: x.strip().split("contain"), f.readlines()):
            k = k[:-6]
            rules[k] = tuple(((int(x[0]), x[1]) for x in bagex.findall(v)))
    return rules


def part1(rules):
    @cache
    def bag_deep_dive(bag, target="shiny gold"):
        if bag == target:
            return True
        if not rules[bag]:
            return False
        return any(bag_deep_dive(color) for _, color in rules[bag])

    return sum(bag_deep_dive(bag) for bag in rules.keys()) - 1


def part2(rules, starting_bag="shiny gold"):
    def how_many(bag):
        if not rules[bag]:
            return False
        else:
            return sum((n + how_many(inner) * n for n, inner in rules[bag]))

    return how_many(starting_bag)


def main():
    parsed = parse_rules("input")
    print(f"part1: {part1(parsed)}")  # 121
    print(f"part2: {part2(parsed)}")  # 3805


if __name__ == "__main__":
    main()
