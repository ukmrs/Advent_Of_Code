#!/usr/bin/env python3

with open("input") as f:
    expenses = [int(num.strip()) for num in f.readlines()]


def part1(expenses, target=2020):
    seen = set()
    for value in expenses:
        if target - value in seen:
            return value * (target - value)
        seen.add(value)


def part2(expenses: set):
    expenses = set(expenses)
    target = 2020
    for a in expenses:
        for b in expenses:
            if target - a - b in expenses:
                return a * b * (target - a - b)


print(f"part1: {part1(expenses)}")  # 858496
print(f"part2: {part2(expenses)}")  # 263819430
