from utils import common
from math import prod


MAX_ALLOWED = {"green": 13, "blue": 14, "red": 12}
BASE = {k: 0 for k in MAX_ALLOWED.keys()}


def iter_cubes(cubes: str):
    samples = cubes.split("; ")
    for sample in samples:
        for cube in sample.split(", "):
            num, color = cube.split()
            yield int(num), color


def calc_line1(line: str) -> int:
    game, cubes = line.split(": ")

    for num, color in iter_cubes(cubes):
        if MAX_ALLOWED[color] < int(num):
            return 0

    return int(game.split()[-1])


def part1(lines: list[str]) -> int:
    return sum(calc_line1(line) for line in lines)


def calc_line2(line: str) -> int:
    cube_dict = BASE.copy()
    _, cubes = line.split(": ")

    for num, color in iter_cubes(cubes):
        cube_dict[color] = max(cube_dict[color], num)

    return prod(cube_dict.values())


def part2(lines: list[str]):
    return sum(calc_line2(line) for line in lines)


def main():
    lines = common.get_input(__file__)
    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
    main()
