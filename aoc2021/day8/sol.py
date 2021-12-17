#!/usr/bin/env python3
from typing import List, Dict
from collections import defaultdict

UNIQUE_SEGMENTS = {2, 3, 4, 7}


LETTERS_TABLE = {
    "cf": 1,
    "acf": 7,
    "bcdf": 4,
    "acdeg": 2,
    "acdfg": 3,
    "abdfg": 5,
    "abcefg": 0,
    "abdefg": 6,
    "abcdfg": 9,
    "abcdefg": 8,
}


class Entry:
    def __init__(self, unique, output):
        self.unique = unique
        self.output = output

    def count_output_uniques(self):
        co = 0
        for number in self.output:
            if len(number) in UNIQUE_SEGMENTS:
                co += 1
        return co

    def solve_row(self):
        return int("".join(self.translate()))

    def translate(self):
        translator = self.identify()

        for number in self.output:
            decoded = "".join(sorted(number.translate(translator)))
            yield str(LETTERS_TABLE[decoded])

    def identify(self) -> Dict[int, int]:
        translator = {k: "x" for k in "abcdefg"}
        hm = defaultdict(list)
        for number in self.unique:
            hm[len(number)].append(set(number))

        one = hm[2][0]
        bd = hm[4][0] - one

        for i in hm[6]:
            ans = one - i
            ans_bd = bd - i
            # get c and f
            if len(ans) == 1:
                letter_c = ans.pop()
                letter_f = one - set(letter_c)
                translator["f"] = letter_f.pop()
                translator["c"] = letter_c

            # get b and d
            if len(ans_bd) == 1:
                letter_d = ans_bd.pop()
                letter_b = bd - set(letter_d)
                translator["b"] = letter_b.pop()
                translator["d"] = letter_d

        # get a
        letter_a = hm[3][0] - one
        translator["a"] = letter_a.pop()

        # get g
        podloze = {translator[i] for i in "acdbf"}

        for i in hm[5]:
            ans = i - podloze
            if len(ans) == 1:
                letter_g = ans.pop()
                translator["g"] = letter_g
                break

        # get e
        podloze = {translator[i] for i in "abcdfg"}
        letter_e = hm[7][0] - podloze
        translator["e"] = letter_e.pop()

        # I was doing it the other way around but it doesnt matter c:
        return {ord(v): ord(k) for k, v in translator.items()}


def parse(file):
    for line in file.readlines():
        unique, output = line.strip().split("|")
        unique = unique.strip()
        output = output.strip()
        yield Entry(unique.split(" "), output.split(" "))


with open("./example") as f:
    EXAMPLE = list(parse(f))

with open("./input") as f:
    INPUT = list(parse(f))


def solve(entries: List[Entry]):
    co = 0
    for entry in entries:
        co += entry.count_output_uniques()
    return co


def solve2(entries: List[Entry]):
    result = 0
    for entry in entries:
        result += entry.solve_row()

    return result


def test():
    solution = solve(EXAMPLE)
    example_sol = 26
    assert solution == example_sol, f"{example_sol} != {solution}"

    solution = solve2(EXAMPLE)
    example_sol = 61229
    assert solution == example_sol, f"{example_sol} != {solution}"


def main():
    test()

    solution = solve(INPUT)
    print(solution)

    solution = solve2(INPUT)
    print(solution)


if __name__ == "__main__":
    main()
