#!/usr/bin/env python3


with open("input") as f:
    forms = [line.rstrip() for line in f.read().rstrip().split("\n\n")]


def part1(forms):
    total = 0
    for form in forms:
        total += len(set(form.replace("\n", "")))
    return total


def part2(forms):
    total = 0
    for form in forms:
        form = form.split("\n")
        everyone = set(form[0])
        for someone in form[1:]:
            everyone &= set(someone)
        total += len(everyone)
    return total


print(part1(forms))  # 6532
print(part2(forms))  # 3427
