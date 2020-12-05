#!/usr/bin/env python3

with open("input") as f:
    case = set()
    to_binary = {ord(char): bl for char, bl in zip("BRFL", "1100")}
    for line in f.readlines():
        case.add(int(line.strip().translate(to_binary), 2))


def part1(bpasses):
    return max(bpasses)


def part2(bpasses):
    max_sid = part1(bpasses)
    for sid in range(max_sid, -1, -1):
        if sid not in case:
            return sid


print(f"part1: {part1(case)}")  # 996
print(f"part2: {part2(case)}")  # 671
