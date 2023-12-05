#!/usr/bin/env python3
from pathlib import Path
from utils import common

#!/usr/bin/env python3
import re


rev = "eno|owt|eerht|ruof|evif|xis|neves|thgie|enin"
ser = "one|two|three|four|five|six|seven|eight|nine"
REX = re.compile(r"\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin")
FEX = re.compile(r"\d|one|two|three|four|five|six|seven|eight|nine")

D = {
    "eno": "1",
    "owt": "2",
    "eerht": "3",
    "ruof": "4",
    "evif": "5",
    "xis": "6",
    "neves": "7",
    "thgie": "8",
    "enin": "9",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def calc_line1(line: str) -> int:
    digit_gen = (i for i in line if i.isdigit())
    first = next(digit_gen)
    last = first
    for c in digit_gen:
        last = c

    return int(first) * 10 + int(last)


def part1(lines):
    return sum(calc_line1(line) for line in lines)


def calc_line2(line: str) -> int:
    tots = ""
    resf = FEX.search(line).group(0)  # type: ignore
    resr = REX.search(line[::-1]).group(0)  # type: ignore

    for c in (resf, resr):
        try:
            tots += D[c]
        except KeyError:
            tots += c

    return int(tots)


def part2(lines: list[str]) -> int:
    return sum(calc_line2(line) for line in lines)


def main():
    lines = common.get_input(__file__)
    print(part1(lines))
    print(part2(lines))


if __name__ == "__main__":
    main()
