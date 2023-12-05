from utils import common
from dataclasses import dataclass
from math import prod


COORDS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))


def any_symbols(text: str):
    for c in text:
        if c.isdigit() or c == ".":
            continue
        return True
    return False


@dataclass
class Number:
    start: int
    end: int
    row: int

    def resolve(self, lines: list[str]) -> int:
        start = self.start - 1 if self.start > 0 else self.start
        end = self.end + 1

        if self.row > 0:
            if any_symbols(lines[self.row - 1][start:end]):
                return self.get_number(lines)

        if self.row + 1 < len(lines):
            if any_symbols(lines[self.row + 1][start:end]):
                return self.get_number(lines)

        if any_symbols(lines[self.row][start:end]):
            return self.get_number(lines)

        return 0

    def get_number(self, lines):
        num = int(lines[self.row][self.start : self.end])
        return num


def part1(lines: list[str]) -> int:
    digit_count = 0
    s = 0

    for i, row in enumerate(lines):
        for j, cell in enumerate(row):
            if cell.isdigit():
                digit_count += 1
                continue

            if digit_count > 0:
                s += Number(j - digit_count, j, i).resolve(lines)

            digit_count = 0

        if digit_count > 0:
            s += Number(len(row) - digit_count, len(row), i).resolve(lines)
            digit_count = 0

    return s


@dataclass
class StarNumber:
    row: int
    col: int

    def expand(self, lines) -> int:
        line = lines[self.row]
        left = self.expand_left(line)
        right = self.expand_right(line)
        return int(line[left : right + 1])

    def expand_left(self, line: str) -> int:
        i = self.col
        for i in range(self.col - 1, -1, -1):
            if not line[i].isdigit():
                return i + 1
        return i

    def expand_right(self, line: str) -> int:
        i = self.col
        for i in range(self.col + 1, len(line)):
            if not line[i].isdigit():
                return i - 1
        return i


def analyze_star_row(row, col, lines) -> list[StarNumber]:
    if col == 0:
        digit_pattern = tuple(i.isdigit() for i in lines[row][col : col + 2])
        col = 1
    else:
        digit_pattern = tuple(i.isdigit() for i in lines[row][col - 1 : col + 2])
        if digit_pattern == (True, False, True):
            return [StarNumber(row, col - 1), StarNumber(row, col + 1)]

    for i, digit in enumerate(digit_pattern):
        if digit:
            return [StarNumber(row, col + i - 1)]

    return []


def resolve_star(row, col, lines) -> int:
    star_numbers = []

    if row > 0:
        star_numbers.extend(analyze_star_row(row - 1, col, lines))

    if row + 1 < len(lines):
        star_numbers.extend(analyze_star_row(row + 1, col, lines))

    if col > 0 and lines[row][col - 1].isdigit():
        star_numbers.append(StarNumber(row, col - 1))

    if col + 1 < len(lines[0]) and lines[row][col + 1].isdigit():
        star_numbers.append(StarNumber(row, col + 1))

    if len(star_numbers) == 2:
        return prod(n.expand(lines) for n in star_numbers)

    return 0


def part2(lines: list[str]) -> int:
    s = 0
    for i, row in enumerate(lines):
        for j, cell in enumerate(row):
            if cell == "*":
                s += resolve_star(i, j, lines)

    return s


def main():
    lines = common.get_input(__file__)
    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
    main()
