#!/usr/bin/env python3
from typing import List
import numpy as np
from time import time

EXAMPLE = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
with open("./input") as f:
    INPUT = [int(i) for i in f.readline().rstrip().split(",")]


def addfact(number):
    return (number ** 2 + number) // 2


def solve2(crustceans: List[int]):
    arr = np.array(crustceans)
    mn, mx = np.min(arr), np.max(arr)
    search_range = np.arange(mn, mx)[:, np.newaxis]

    b = np.abs(arr - search_range)
    b = np.vectorize(addfact)(b)
    return np.min(np.sum(b, axis=1))


def solve(crustceans: List[int]):
    arr = np.array(crustceans)
    mn, mx = np.min(arr), np.max(arr)
    search_range = np.arange(mn, mx)[:, np.newaxis]

    b = np.abs(arr - search_range)
    return np.min(np.sum(b, axis=1))


def test():
    solution = solve(EXAMPLE)
    example_sol = 37
    assert solution == example_sol, f"{example_sol} != {solution}"

    solution = solve2(EXAMPLE)
    example_sol = 168
    assert solution == example_sol, f"{example_sol} != {solution}"


def main():
    test()
    solution1 = solve(INPUT)
    print(solution1)

    solution2 = solve2(INPUT)
    print(solution2)


if __name__ == "__main__":
    main()
