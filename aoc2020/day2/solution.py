#!/usr/bin/env python3
import fileinput
import re

database = [line.strip().split(": ") for line in fileinput.input("input")]
rex = re.compile(r"(\d+)-(\d+)\s([a-z])")


def part1(db):
    result = 0
    for policy, pw in db:
        a, b, char = rex.search(policy).groups()
        if int(a) <= pw.count(char) <= int(b):
            result += 1

    return result


def part2(db):
    valid = 0
    for policy, pw in db:
        a, b, char = rex.search(policy).groups()
        a, b = int(a) - 1, int(b) - 1
        critical = pw[a] + pw[b]
        if critical.count(char) == 1:
            valid += 1

    return valid


# print(part1(database))
print(part2(database))
