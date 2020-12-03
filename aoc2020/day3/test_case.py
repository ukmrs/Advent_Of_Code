from solution import toboggan
from math import prod

case = [
    "..##.......", "#...#...#..", ".#....#..#.", "..#.#...#.#", ".#...##..#.",
    "..#.##.....", ".#.#.#....#", ".#........#", "#.##...#...", "#...##....#",
    ".#..#...#.#"
]


def test_part1():
    assert sum(toboggan(case, [(3, 1)])) == 7


def test_part2():
    p2 = prod(toboggan(case, ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))))
    assert p2 == 336
