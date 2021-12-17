#!/usr/bin/env python3
from collections import defaultdict, namedtuple
from typing import List
from enum import Enum
import re


class Orientation(Enum):
    horizontal = 1
    vertical = 2
    diagonal = 3


numex = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")

Line = namedtuple("Line", ["anchor", "line", "orientation"])


class Coordinate:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)

    def __repr__(self):
        return f"{self.x1},{self.y1} => {self.x2},{self.y2}"

    def get_line(self):
        if self.x1 == self.x2:
            return Line(self.x1, self.vertical_line(), Orientation.vertical)
        elif self.y1 == self.y2:
            return Line(self.y1, self.horizontal_line(), Orientation.horizontal)
        return None

    def get_line2(self):
        if self.x1 == self.x2:
            return Line(self.x1, self.vertical_line(), Orientation.vertical)
        elif self.y1 == self.y2:
            return Line(self.y1, self.horizontal_line(), Orientation.horizontal)
        return Line(*self.diagonal_line(), Orientation.diagonal)

    def diagonal_line(self):
        return (self.horizontal_line(), self.vertical_line())

    def horizontal_line(self):
        if self.x2 > self.x1:
            return range(self.x1, self.x2 + 1)
        return range(self.x1, self.x2 - 1, -1)

    def vertical_line(self):
        if self.y2 > self.y1:
            return range(self.y1, self.y2 + 1)
        return range(self.y1, self.y2 - 1, -1)


def solve1(parsed: List[Coordinate]):
    return solve(parsed, Coordinate.get_line)


def solve2(parsed: List[Coordinate]):
    return solve(parsed, Coordinate.get_line2)


def solve(parsed: List[Coordinate], func):
    rows = defaultdict(dict)
    count = 0
    
    for co in parsed:
        line = func(co)
        if line is None:
            continue

        if line.orientation == Orientation.horizontal:
            for ix in line.line:
                res = rows[line.anchor].get(ix, 0) + 1
                rows[line.anchor][ix] = res
                if res == 2:
                    count += 1

        elif line.orientation == Orientation.vertical:
            for ix in line.line:
                res = rows[ix].get(line.anchor, 0) + 1
                rows[ix][line.anchor] = res
                if res == 2:
                    count += 1

        elif line.orientation == Orientation.diagonal:
            for hix, vix in zip(line.anchor, line.line):
                res = rows[vix].get(hix, 0) + 1
                rows[vix][hix] = res
                if res == 2:
                    count += 1

    return count


def parse_file(file):
    result = []
    with open(file, "r") as f:
        for line in f.readlines():
            found = numex.search(line.strip())
            if found is not None:
                result.append(Coordinate(*found.groups()))
    return result


def test():
    parsed = parse_file("./example")
    assert solve1(parsed) == 5
    assert solve2(parsed) == 12


def main():
    test()
    parsed = parse_file("./input")
    solution1 = solve1(parsed)
    solution2 = solve2(parsed)
    print(solution1)
    print(solution2)




if __name__ == "__main__":
    main()
