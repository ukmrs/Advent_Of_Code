#!/usr/bin/env python3
from collections import deque


def parse_xmas_data(data_file):
    with open(data_file) as f:
        return [int(i) for i in f.readlines()]


def part1(data, preamble):
    que = deque(data[:preamble])
    relevant = set(que)
    for num in data[preamble:]:
        for rel in relevant:
            if abs(rel - num) in relevant:
                break
        else:
            return num
        relevant.remove(que.popleft())
        que.append(num)
        relevant.add(num)


def part2(data, target):
    tail, wels = 0, 0
    for ix, num in enumerate(data):
        wels += num
        while wels > target:
            wels -= data[tail]
            tail += 1
        if wels == target:
            return min(data[tail:ix+1]) + max(data[tail:ix+1])


def main():
    parsed = parse_xmas_data("input")
    ans1 = part1(parsed, 25)
    ans2 = part2(parsed, ans1)

    print(f"part1: {ans1}")  # 217430975
    print(f"part2: {ans2}")  # 28509180


if __name__ == "__main__":
    main()
