#!/usr/bin/env python3
import fileinput

INPUT = "input.txt"
expenses = [int(num.strip()) for num in fileinput.input(INPUT)]


def part1(expenses, target=2020):
    seen = set()
    for value in expenses:
        if target - value in seen:
            return value * (target - value)
        seen.add(value)


expenses = set((int(num.strip()) for num in fileinput.input(INPUT)))


def part2(expenses: set):
    target = 2020
    for a in expenses:
        for b in expenses:
            if target - a - b in expenses:
                return a * b * (target - a - b)


print(part1(expenses))
print(part2(expenses))
