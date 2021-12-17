#!/usr/bin/env python3
from typing import List, Dict

EXAMPLE = [3, 4, 3, 1, 2]
with open("./input") as f:
    INPUT = [int(i) for i in f.readline().rstrip().split(",")]


def resolve_day(ocean: Dict[int, int]):
    tmp = 0

    births = ocean[0]

    for i in range(8, -1, -1):
        ocean[i], tmp = tmp, ocean[i]

    ocean[8] += births
    ocean[6] += births


def solve(fishes: List[int], days: int):
    ocean = {i: 0 for i in range(0, 9)}
    for fish in fishes:
        ocean[fish] += 1
    for _ in range(days):
        resolve_day(ocean)

    return sum(ocean.values())


def test():
    solution = solve(EXAMPLE, 80)
    assert solution == 5934

    solution = solve(EXAMPLE, 256)
    assert solution == 26984457539


def main():
    test()
    solution1 = solve(INPUT, 80)
    print(solution1)
    solution2 = solve(INPUT, 256)
    print(solution2)


if __name__ == "__main__":
    main()
