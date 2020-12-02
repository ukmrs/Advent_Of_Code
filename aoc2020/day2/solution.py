#!/usr/bin/env python3
import fileinput
import re

database = [line.strip() for line in fileinput.input("input")]


def part1(db):
    result = 0
    rex = re.compile(r"(\d+)-(\d+)\s([a-z])")
    for entry in db:
        policy, pw = entry.split(": ")
        a, b, char = rex.search(policy).groups()
        if int(a) <= pw.count(char) <= int(b):
            result += 1

    return result


def part2():
    ...


print(part1(database))
