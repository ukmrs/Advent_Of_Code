#!/usr/bin/env python3
LOWER = {"F": True, "L": True, "B": False, "R": False}


def get_rc(partitioning: str) -> int:
    lb, hb = 0, 2**(len(partitioning)) - 1
    for char in partitioning:
        if LOWER[char]:
            hb -= -((hb - lb) // -2)
        else:
            lb += -((hb - lb) // -2)
    return lb


with open("input") as f:
    case = []
    for line in f.readlines():
        line = line.strip()
        row, col = get_rc(line[:7]), get_rc(line[7:])
        case.append((row, col))


def part1(bpasses):
    mx = float("-INF")
    for bpass in bpasses:
        row, col = bpass
        mx = max(row * 8 + col, mx)
    return mx


def part2(bpasses):
    out_of_bounds = part1(bpasses)
    max_row = out_of_bounds // 8
    bset = {i[0] * 8 + i[1] for i in bpasses}
    for row in range(max_row, -1, -1):
        for col in range(8):
            if (sid := row * 8 + col) not in bset:
                if sid < out_of_bounds:  # max_row + higher col than possible
                    return sid


print(f"part1: {part1(case)}")  # 996
print(f"part2: {part2(case)}")  # 671
